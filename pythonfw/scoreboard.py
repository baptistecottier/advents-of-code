#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Render the scoreboards from events/benchmarks.json (written by pythonfw/benchmark.py):
the summary on the homepage, between the scoreboard markers of README.md, and one
detailed page per year, events/year_YYYY/README.md. A result measured on code that differs
from the last commit is marked †, so the published scoreboard never hides it.

    python pythonfw/scoreboard.py
"""

# Standard import
import ast
import datetime
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVENTS = ROOT / "events"
RESULTS = EVENTS / "benchmarks.json"
README = ROOT / "README.md"
MARKERS = ("<!-- scoreboard:start -->", "<!-- scoreboard:end -->")

LANGUAGES = {"python": ("Python", "py"), "rust": ("Rust", "rs")}
FAST = 10  # seconds
NBSP = " "  # keeps strips on one line, and an unsolved day an empty box
SYMBOLS = {"fast": "█", "slow": "▓", "partial": "░", "unsolved": NBSP}


# ===========================================================================
# Day states
# ===========================================================================

def days_in(year: int) -> int:
    """Number of puzzles in a given year: 25 until 2024, 12 from 2025 on."""
    return 12 if year >= 2025 else 25


def stars(year: int, days: dict, language: str) -> dict[int, list[str]]:
    """
    Per day, the state of each star: 'ok', 'unknown' (answer not known locally) or
    'no'. The final day's second star is free once every other star is earned.
    """
    result = {}
    for day in range(1, days_in(year) + 1):
        parts = days.get(str(day), {}).get(language, {}).get("parts", [])
        result[day] = [part if part in ("ok", "unknown") else "no" for part in parts]
        result[day] += ["no"] * (2 - len(result[day]))
    final = days_in(year)
    others = all(part == "ok" for day, parts in result.items() if day != final for part in parts)
    result[final][1] = "ok" if others and result[final][0] == "ok" else "no"
    return result


def state(result: dict | None, day_stars: list[str]) -> str:
    """One of 'fast', 'slow', 'partial' or 'unsolved' (also when there is no solution)."""
    if result is None:
        return "unsolved"
    if result["status"] == "solved":
        return "fast" if result["time"] < FAST else "slow"
    return "partial" if "ok" in day_stars else "unsolved"


def format_time(seconds: float) -> str:
    """Human-readable duration: 0.4 ms, 12 ms, 3.2 s, 1 min 05 s."""
    if seconds < 0.001:
        return "< 1 ms"
    if seconds < 1:
        return f"{seconds * 1000:.0f} ms"
    if seconds < 60:
        return f"{seconds:.1f} s"
    minutes, seconds = divmod(round(seconds), 60)
    return f"{minutes} min {seconds:02} s" if seconds else f"{minutes} min"


# ===========================================================================
# Code fingerprints
# ===========================================================================

def solution_files(year: int, day: int, language: str) -> list[Path]:
    """
    Files a result depends on: the solution, plus the repository modules it imports
    (Python) or the aoc library behind its main! macro (Rust).
    """
    path = EVENTS / f"year_{year}/day_{day:02}/day_{day:02}.{LANGUAGES[language][1]}"
    if language == "rust":
        return [path, ROOT / "rustfw/src/lib.rs"]
    files, todo = [path], [path]
    while todo:
        module = todo.pop()
        try:
            tree = ast.parse(module.read_text(encoding="utf-8"))
        except (OSError, SyntaxError, ValueError):
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
                names = [node.module] + [f"{node.module}.{alias.name}" for alias in node.names]
            else:
                continue
            for name in names:
                relative = name.replace(".", "/") + ".py"
                for candidate in (ROOT / relative, module.parent / relative):
                    if candidate.is_file() and candidate not in files:
                        files.append(candidate)
                        todo.append(candidate)
    return files


def _git_blob(path: Path) -> str | None:
    """Git object id of a file as it is in the working tree."""
    try:
        data = path.read_bytes()
    except OSError:
        return None
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def committed_blobs() -> dict[str, str] | None:
    """Git object id of every file of the last commit, by path; None outside of git."""
    try:
        listing = subprocess.run(["git", "ls-tree", "-r", "-z", "HEAD"], cwd=ROOT, check=True,
                                 capture_output=True, text=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return None
    entries = (entry.split("\t", 1) for entry in listing.split("\0") if entry)
    return {path: meta.split()[2] for meta, path in entries}


def fingerprint(files: list[Path], blobs: dict[str, str] | None = None) -> str | None:
    """
    Short hash identifying the code behind a result: as in the working tree, or as in
    the last commit when its blobs are given. None if a file is missing.
    """
    ids = []
    for path in sorted(files):
        relative = path.relative_to(ROOT).as_posix()
        blob = _git_blob(path) if blobs is None else blobs.get(relative)
        if blob is None:
            return None
        ids.append(f"{relative} {blob}")
    return hashlib.sha1("\n".join(ids).encode()).hexdigest()[:12]


def uncommitted(results: dict) -> set[tuple[str, str, str]]:
    """(year, day, language) of the results measured on code that is not the committed one."""
    blobs = committed_blobs()
    if blobs is None:
        return set()
    return {(year, day, language)
            for year, days in results["years"].items() for day, entry in days.items()
            for language in LANGUAGES if language in entry
            and entry[language].get("code")
            != fingerprint(solution_files(int(year), int(day), language), blobs)}


# ===========================================================================
# Pages
# ===========================================================================

def year_summary(year: int, days: dict, language: str) -> dict:
    """Stars, state of every day and total solving time of a language for a year."""
    year_stars = stars(year, days, language)
    states = [state(days.get(str(day), {}).get(language), year_stars[day])
              for day in range(1, days_in(year) + 1)]
    solved = [days[str(day)][language]["time"] for day, s in enumerate(states, 1)
              if s in ("fast", "slow")]
    return {"stars": sum(part == "ok" for parts in year_stars.values() for part in parts),
            "max": 2 * days_in(year), "states": states, "time": sum(solved),
            "day_stars": year_stars}


def symbol(day_state: str) -> str:
    """Symbol of a day state, always in the code font, so that it looks the same as in
    the strips: block characters are drawn very differently from one font to another."""
    return f"`{SYMBOLS[day_state]}`"


def strip(states: list[str]) -> str:
    """One symbol per day, as one inline code span per block of five days."""
    symbols = "".join(SYMBOLS[s] for s in states)
    return NBSP.join(f"`{symbols[i:i + 5]}`" for i in range(0, len(symbols), 5))


def legend(separator: str = " · ") -> str:
    """Meaning of the day symbols."""
    return separator.join([f"{symbol('fast')} solved in under {FAST} s",
                           f"{symbol('slow')} solved in under 5 min",
                           f"{symbol('partial')} one part only",
                           f"{symbol('unsolved')} not solved"])


def environment(meta: dict) -> str:
    """Where and when the benchmark ran."""
    parts = []
    if meta.get("python"):
        parts.append(f"Python {meta['python']}")
    if meta.get("rust"):
        parts.append(f"Rust {meta['rust']} (release)")
    if meta.get("machine"):
        parts.append(meta["machine"])
    if meta.get("date"):
        parts.append(datetime.date.fromisoformat(meta["date"]).strftime("%-d %B %Y"))
    return " · ".join(parts)


def homepage(results: dict, flagged: set) -> str:
    """Scoreboard block of the homepage: one row per year, one strip per language."""
    header = "| Year | " + " | ".join(f"{name} | ★" for name, _ in LANGUAGES.values()) + " |"
    lines = [header, "| :-- | " + " | ".join(":-- | --:" for _ in LANGUAGES) + " |"]
    totals = {language: {"stars": 0, "max": 0, "states": []} for language in LANGUAGES}
    for year in sorted(results["years"], key=int, reverse=True):
        cells = [f"[{year}](events/year_{year}/README.md)"]
        for language in LANGUAGES:
            summary = year_summary(int(year), results["years"][year], language)
            cells += [strip(summary["states"]), f"{summary['stars']}/{summary['max']}"]
            for key in ("stars", "max"):
                totals[language][key] += summary[key]
            totals[language]["states"] += summary["states"]
        lines.append("| " + " | ".join(cells) + " |")

    cells = ["**Total**"]
    for total in totals.values():
        counts = " ".join(f"{symbol(s)} {total['states'].count(s)}"
                          for s in ("fast", "slow", "partial", "unsolved"))
        cells += [counts, f"**{total['stars']}/{total['max']}**"]
    lines.append("| " + " | ".join(cells) + " |")

    notes = [legend(" &emsp; ")]
    if flagged:
        notes.append(f"{len(flagged)} result(s) measured on uncommitted code, "
                     "marked † on the year pages")
    notes.append(environment(results["meta"]))
    return "\n".join([
        "## Scoreboard", "",
        *lines, "",
        f"<sub>{'<br>'.join(notes)}</sub>",
    ])


def stars_cell(day_stars: list[str]) -> str:
    """★ earned, ☆ not earned, ? answer unknown locally (cannot be verified)."""
    return "".join({"ok": "★", "no": "☆", "unknown": "?"}[part] for part in day_stars)


def time_cell(result: dict, timeout: float) -> str:
    """Solving time, or why there is none."""
    if result["status"] == "timeout":
        return f"> {format_time(timeout)}"
    if result["time"] is None:
        return "build error" if result.get("error") == "does not compile" else "error"
    return format_time(result["time"])


def navigation(year: int, years: list[int]) -> str:
    """Links to the previous year, the scoreboard and the next year."""
    links = []
    if year - 1 in years:
        links.append(f"[← {year - 1}](../year_{year - 1}/README.md)")
    links.append("[Scoreboard](../../README.md#scoreboard)")
    if year + 1 in years:
        links.append(f"[{year + 1} →](../year_{year + 1}/README.md)")
    return " · ".join(links)


def summary_table(summaries: dict) -> list[str]:
    """Stars, number of days in each state and solving time, per language."""
    rows = [("Stars", lambda s: f"{s['stars']}/{s['max']}")]
    rows += [(label, lambda s, key=key: str(s["states"].count(key)))
             for key, label in [("fast", f"{symbol('fast')} solved in under {FAST} s"),
                                ("slow", f"{symbol('slow')} solved in under 5 min"),
                                ("partial", f"{symbol('partial')} one part only"),
                                ("unsolved", f"{symbol('unsolved')} not solved")]]
    rows.append(("Time of solved days", lambda s: format_time(s["time"]) if s["time"] else "–"))
    lines = ["| | " + " | ".join(name for name, _ in LANGUAGES.values()) + " |",
             "| :-- | " + " | ".join("--:" for _ in LANGUAGES) + " |"]
    return lines + [f"| {label} | " + " | ".join(value(summaries[language])
                                                 for language in LANGUAGES) + " |"
                    for label, value in rows]


def day_table(year: int, days: dict, summaries: dict, timeout: float,
              flagged: set) -> list[str]:
    """One row per day: title, then symbol, stars and time for each language."""
    header = ["Day", "Puzzle"] + [cell for name, _ in LANGUAGES.values() for cell in (name, "")]
    lines = ["| " + " | ".join(header) + " |",
             "| --: | :-- | " + " | ".join(":-- | --:" for _ in LANGUAGES) + " |"]
    for day in range(1, days_in(year) + 1):
        entry = days.get(str(day), {})
        title = entry.get("title") or f"Day {day}"
        cells = [str(day), f"[{title}](https://adventofcode.com/{year}/day/{day})"]
        for language, (_, extension) in LANGUAGES.items():
            day_symbol = symbol(summaries[language]["states"][day - 1])
            day_stars = stars_cell(summaries[language]["day_stars"][day])
            if language not in entry:  # no solution: unsolved, with nothing to link or time
                cells += [f"{day_symbol} {day_stars}", ""]
                continue
            mark = " †" if (str(year), str(day), language) in flagged else ""
            cells += [f"{day_symbol} [{day_stars}](day_{day:02}/day_{day:02}.{extension})",
                      time_cell(entry[language], timeout) + mark]
        lines.append("| " + " | ".join(cells) + " |")
    return lines


def year_page(results: dict, year: int, years: list[int], flagged: set) -> str:
    """Detailed page of a year: summary per language, then one row per day."""
    days = results["years"][str(year)]
    summaries = {language: year_summary(year, days, language) for language in LANGUAGES}

    notes = [legend(" &emsp; ")]
    if any("unknown" in parts for summary in summaries.values()
           for parts in summary["day_stars"].values()):
        notes.append("? no answer recorded by Puzzle Submitter, so it cannot be verified")
    if any(key[0] == str(year) for key in flagged):
        notes.append("† measured on code that differs from the last commit")
    notes.append(environment(results["meta"]))

    return "\n".join([
        f"# Advent of Code {year}", "",
        navigation(year, years), "",
        *summary_table(summaries), "",
        *day_table(year, days, summaries, results["meta"].get("timeout", 300), flagged), "",
        f"<sub>{'<br>'.join(notes)}</sub>", "",
    ])


# ===========================================================================
# Output
# ===========================================================================

def render() -> None:
    """Write the homepage scoreboard and every year page."""
    with open(RESULTS, encoding="utf-8") as f:
        results = json.load(f)
    flagged = uncommitted(results)

    text = README.read_text(encoding="utf-8")
    start, end = MARKERS
    block = f"{start}\n{homepage(results, flagged)}\n{end}"
    pattern = re.compile(re.escape(start) + ".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        raise SystemExit(f"README.md has no {start} … {end} block to fill")
    README.write_text(pattern.sub(lambda _: block, text), encoding="utf-8")

    years = [int(year) for year in results["years"]]
    for year in years:
        page = EVENTS / f"year_{year}" / "README.md"
        page.write_text(year_page(results, year, years, flagged), encoding="utf-8")
    print(f"📝 Scoreboards written: README.md and {len(years)} year page(s)")


if __name__ == '__main__':
    render()
