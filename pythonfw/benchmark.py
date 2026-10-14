#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Benchmark every solution against the known answers, store the results in
events/benchmarks.json and regenerate the scoreboards.

Each day runs in its own process with a timeout (5 minutes by default). The measured
time covers preprocessing and solving, not interpreter start-up, imports or compilation.
Expected answers are the ones the Puzzle Submitter extension recorded as correct, read
from the VS Code workspace state of this repository: a day with no recorded answer cannot
be verified.

Examples:
    python pythonfw/benchmark.py                   # every year, both languages
    python pythonfw/benchmark.py 2024              # one year
    python pythonfw/benchmark.py 2024 --days 1-5   # some days of a year
    python pythonfw/benchmark.py --lang python     # one language
    python pythonfw/benchmark.py --changed         # only code changed since its last run
    python pythonfw/benchmark.py --render          # only regenerate the scoreboards
"""

# Standard import
import argparse
import datetime
import html
import importlib
import json
import os
import platform
import re
import shutil
import signal
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
import urllib.request
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
EVENTS = ROOT / "events"
RESULTS = EVENTS / "benchmarks.json"
INPUT_STORE = ROOT / ".puzzle-submitter" / "aoc.json"
RUST_DIR = ROOT / "rustfw"
LANGUAGES = {"python": "py", "rust": "rs"}
EXTENSION = "baptistecottier.puzzle-submitter"
USER_AGENT = "github.com/baptistecottier/advents-of-code benchmark"


# ===========================================================================
# Calendar
# ===========================================================================

def released_years(today: datetime.date | None = None) -> list[int]:
    """Years whose event has started (AoC starts on December 1st)."""
    today = today or datetime.date.today()
    last = today.year if today.month == 12 else today.year - 1
    return list(range(2015, last + 1))


def days_in(year: int) -> int:
    """Number of puzzles in a given year: 25 until 2024, 12 from 2025 on."""
    return 12 if year >= 2025 else 25


def solution_path(year: int, day: int, language: str) -> Path:
    """Path of the solution file of a given day in a given language."""
    return EVENTS / f"year_{year}/day_{day:02}/day_{day:02}.{LANGUAGES[language]}"


def has_solution(year: int, day: int, language: str) -> bool:
    """Whether a given day has a solution in a given language (an empty file has none)."""
    path = solution_path(year, day, language)
    return path.is_file() and bool(path.read_text(encoding="utf-8").strip())


# ===========================================================================
# Inputs and expected answers
# ===========================================================================

def load_inputs() -> dict:
    """Puzzle inputs from the store shared with the Puzzle Submitter extension."""
    with open(INPUT_STORE, encoding="utf-8") as f:
        return json.load(f)


def puzzle_input(inputs: dict, year: int, day: int) -> str | None:
    """Puzzle input for a given day, without trailing newlines, or None if unknown."""
    value = inputs.get(str(year), {}).get(str(day), {}).get("1")
    return str(value).rstrip('\n') if value else None


def _workspace_storages() -> list[Path]:
    """VS Code's per-workspace storage folders (stable and Insiders, on every platform)."""
    bases = [Path.home() / "Library/Application Support", Path.home() / ".config",
             Path(os.environ.get("APPDATA", Path.home()))]
    return [base / app / "User/workspaceStorage" for base in bases
            for app in ("Code", "Code - Insiders")]


def load_answers() -> dict[tuple[int, int], dict]:
    """
    Answers recorded as correct by Puzzle Submitter for this repository, as
    {(year, day): {"1": answer, "2": answer}}. They live in the extension's workspace
    state, inside the VS Code workspace storage whose folder is this repository.
    """
    answers = {}
    for storage in _workspace_storages():
        for workspace in storage.glob("*/workspace.json"):
            try:
                folder = json.loads(workspace.read_text(encoding="utf-8")).get("folder", "")
            except (OSError, json.JSONDecodeError):
                continue
            if unquote(urlparse(folder).path).rstrip("/") != str(ROOT):
                continue
            database = workspace.with_name("state.vscdb").as_uri() + "?mode=ro"
            try:
                with closing(sqlite3.connect(database, uri=True)) as connection:
                    row = connection.execute("SELECT value FROM ItemTable WHERE key = ?",
                                             (EXTENSION,)).fetchone()
            except sqlite3.Error:
                continue
            state = json.loads(row[0]) if row else {}
            for key, recorded in state.items():
                match = re.fullmatch(r"puzzleSubmitter\.progress\.aoc\.(\d+)\.(\d+)", key)
                if match and isinstance(recorded, dict):
                    answers.setdefault((int(match[1]), int(match[2])), {}).update(recorded)
    return answers


def expected_answers(answers: dict, year: int, day: int) -> list[str | None]:
    """Recorded answers of a given day: one per part, a single one for the final day."""
    recorded = answers.get((year, day), {})
    parts = ("1",) if day == days_in(year) else ("1", "2")
    return [str(recorded[part]).strip() if recorded.get(part) else None for part in parts]


def puzzle_title(year: int, day: int) -> str | None:
    """Title of a given puzzle, from its public page on adventofcode.com."""
    request = urllib.request.Request(f"https://adventofcode.com/{year}/day/{day}",
                                     headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            page = response.read().decode("utf-8")
    except OSError:
        return None
    match = re.search(r"<h2>--- Day \d+: (.+?) ---</h2>", page)
    return html.unescape(match[1]) if match else None


# ===========================================================================
# Python solutions
# ===========================================================================

def _normalise(answer) -> str:
    """String form of an answer, as it would be submitted."""
    if isinstance(answer, float) and answer.is_integer():
        answer = int(answer)
    return str(answer).strip()


def python_child(year: int, day: int) -> None:
    """
    Run one Python solution on the input read from stdin. Each answer is written to
    stdout as a JSON line as soon as it is known, so that a timeout keeps the parts
    already solved. Everything the solution prints is discarded.
    """
    out = os.fdopen(os.dup(1), "w", encoding="utf-8")
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(devnull, 1)
    os.dup2(devnull, 2)

    def emit(**message):
        out.write(json.dumps(message) + "\n")
        out.flush()

    data = sys.stdin.read()
    day_dir = solution_path(year, day, "python").parent
    sys.path[:0] = [str(ROOT), str(day_dir)]
    try:
        module = importlib.import_module(f"day_{day:02}")
        start = time.perf_counter()
        args = module.preprocessing(data) if hasattr(module, "preprocessing") else data
        result = module.solver(*args) if isinstance(args, tuple) else module.solver(args)
        if not isinstance(result, Iterable) or isinstance(result, (str, bytes, dict)):
            result = (result,)
        for item in result:
            if isinstance(item, tuple):  # a (part, answer) pair
                emit(part=str(item[0]), answer=_normalise(item[1]),
                     time=time.perf_counter() - start)
            else:
                emit(answer=_normalise(item), time=time.perf_counter() - start)
        emit(done=time.perf_counter() - start)
    except BaseException as exc:  # pylint: disable=broad-except
        emit(error=f"{type(exc).__name__}: {str(exc)[:200]}")
    out.close()
    os._exit(0)  # do not wait for threads or processes left behind by the solution


def run_python(year: int, day: int, data: str, timeout: float) -> dict:
    """Run one Python solution in its own process and collect its answers."""
    command = [sys.executable, __file__, "--child", str(year), str(day)]
    with subprocess.Popen(command, cwd=ROOT, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                          stderr=subprocess.DEVNULL, text=True,
                          start_new_session=True) as process:
        try:
            output, _ = process.communicate(data, timeout=timeout)
            timed_out = False
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            output, _ = process.communicate()
            timed_out = True
        _kill_group(process.pid)

    answers, total, error = [], None, None
    for line in output.splitlines():
        try:
            message = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "answer" in message:
            part = {"a": 0, "1": 0, "b": 1, "2": 1}.get(message.get("part"), len(answers))
            answers.extend([None] * (part + 1 - len(answers)))
            answers[part] = message["answer"]
        elif "done" in message:
            total = message["done"]
        elif "error" in message:
            error = message["error"]
    if total is not None:  # answered in time, only a leftover process was still running
        timed_out = False
    if not timed_out and total is None and error is None:
        error = f"exited with code {process.returncode}"
    return {"answers": answers, "time": total, "timeout": timed_out, "error": error}


def _kill_group(pgid: int) -> None:
    """Kill whatever a solution left behind in its process group."""
    try:
        os.killpg(pgid, signal.SIGKILL)
    except (ProcessLookupError, PermissionError):
        pass


# ===========================================================================
# Rust solutions
# ===========================================================================

def rust_toolchain() -> str | None:
    """Path to cargo, if a Rust toolchain is installed."""
    return shutil.which("cargo") or next(
        (str(p) for p in [Path.home() / ".cargo/bin/cargo"] if p.is_file()), None)


def build_rust(cargo: str, days: list[tuple[int, int]]) -> dict[str, Path]:
    """
    Build the given Rust solutions in release mode and return their binaries by name.
    Only binaries cargo reports as built from the current sources are kept, so a solution
    that no longer compiles has no binary rather than a stale one.
    """
    print(f"🦀 Building {len(days)} Rust solution(s) (release)...", flush=True)
    targets = [arg for year, day in days for arg in ("--bin", f"{year}-{day:02}")]
    build = subprocess.run([cargo, "build", "--release", "--keep-going", "--quiet",
                            "--message-format=json-render-diagnostics", *targets],
                           cwd=RUST_DIR, check=False, capture_output=True, text=True)
    binaries = {}
    for line in build.stdout.splitlines():
        message = json.loads(line)
        if message.get("reason") == "compiler-artifact" and message.get("executable"):
            binaries[message["target"]["name"]] = Path(message["executable"])
    return binaries


def parse_rust_output(output: str) -> list[str]:
    """Answers printed by a Rust solution: a debug-printed tuple, or one per line."""
    output = output.strip()
    if output.startswith("(") and output.endswith(")"):
        outside_quotes = r',\s*(?=(?:[^"]*"[^"]*")*[^"]*$)'
        return [part.strip().strip('"') for part in re.split(outside_quotes, output[1:-1])
                if part.strip()]
    labelled = re.findall(r"(?im)^\s*part\s*[12ab]\s*:\s*(.+?)\s*$", output)
    return labelled or [line.strip() for line in output.splitlines() if line.strip()]


def run_rust(binary: Path | None, year: int, day: int, data: str, timeout: float) -> dict:
    """
    Run one compiled Rust solution. Solutions read ../events/year_YYYY/day_DD/day_DD.input
    relative to their working directory, so they run from a scratch directory holding the
    input from the store, leaving the local .input files untouched.
    """
    if binary is None:
        return {"answers": [], "time": None, "timeout": False, "error": "does not compile"}
    scratch = Path(tempfile.mkdtemp(prefix="aoc-bench-"))
    input_path = scratch / f"events/year_{year}/day_{day:02}/day_{day:02}.input"
    input_path.parent.mkdir(parents=True)
    input_path.write_text(data, encoding="utf-8")
    (scratch / "rustfw").mkdir()
    # macOS scans a binary on its first launch: launch it once untimed, from a directory
    # where it finds no input and stops at once
    try:
        subprocess.run([binary], cwd=scratch, stdin=subprocess.DEVNULL, capture_output=True,
                       timeout=10, check=False)
    except subprocess.TimeoutExpired:
        pass

    start = time.perf_counter()
    with subprocess.Popen([binary], cwd=scratch / "rustfw", stdin=subprocess.DEVNULL,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                          start_new_session=True) as process:
        try:
            output, errors = process.communicate(timeout=timeout)
            elapsed, timed_out = time.perf_counter() - start, False
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            output, errors = process.communicate()
            elapsed, timed_out = None, True
    shutil.rmtree(scratch, ignore_errors=True)
    if not timed_out and process.returncode != 0:
        lines = errors.strip().splitlines()
        return {"answers": [], "time": None, "timeout": False,
                "error": lines[-1][:200] if lines else f"exited with code {process.returncode}"}
    return {"answers": parse_rust_output(output) if not timed_out else [],
            "time": elapsed, "timeout": timed_out, "error": None}


# ===========================================================================
# Benchmark
# ===========================================================================

def grade(run: dict, expected: list[str | None]) -> dict:
    """Compare a run with the expected answers and keep what the scoreboard needs."""
    parts = []
    for index, answer in enumerate(expected):
        given = run["answers"][index] if index < len(run["answers"]) else None
        if given is None:
            parts.append("missing")
        elif answer is None:
            parts.append("unknown")
        else:
            parts.append("ok" if given == answer else "wrong")
    if run["timeout"]:
        status = "timeout"
    elif run["error"]:
        status = "error"
    elif all(part == "ok" for part in parts):
        status = "solved"
    else:
        status = "wrong"
    result = {"status": status, "parts": parts,
              "time": round(run["time"], 4) if run["time"] is not None else None,
              "date": datetime.date.today().isoformat()}
    if run["error"]:
        result["error"] = run["error"]
    return result


def load_results() -> dict:
    """Previous benchmark results, so that a partial run only updates what it ran."""
    if RESULTS.is_file():
        with open(RESULTS, encoding="utf-8") as f:
            return json.load(f)
    return {"meta": {}, "years": {}}


def save_results(results: dict) -> None:
    """Write the benchmark results, sorted and with one line per day so diffs stay readable."""
    years = []
    for year, days in sorted(results["years"].items()):
        lines = [f'    "{day}": {json.dumps(entry, ensure_ascii=False)}'
                 for day, entry in sorted(days.items(), key=lambda item: int(item[0]))]
        years.append(f'  "{year}": {{\n' + ",\n".join(lines) + "\n  }")
    with open(RESULTS, "w", encoding="utf-8") as f:
        f.write('{\n  "meta": ' + json.dumps(results["meta"], ensure_ascii=False) + ',\n')
        f.write('  "years": {\n' + ",\n".join(years) + "\n  }\n}\n")


def describe(result: dict) -> str:
    """One-line summary of a result for the console."""
    stars = "".join("★" if part == "ok" else "☆" for part in result["parts"])
    if result["status"] == "timeout":
        return f"{stars} timeout"
    if result["time"] is None:
        return f"{stars} {result.get('error', result['status'])}"
    return f"{stars} {result['time']:.3f}s {result['status']}"


def machine() -> str:
    """Short description of the machine running the benchmark."""
    try:
        cpu = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"], check=True,
                             capture_output=True, text=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        cpu = platform.processor() or platform.machine()
    return cpu


def outdated(result: dict | None, code: str | None, expected: list[str | None]) -> bool:
    """
    Whether a result needs a new run: never measured, measured on other code, or with an
    answer that could not be verified then but can be now.
    """
    if result is None or result.get("code") != code:
        return True
    return any(part == "unknown" and answer is not None
               for part, answer in zip(result["parts"], expected))


def benchmark(years: list[int], days: list[int] | None, languages: list[str],
              timeout: float, jobs: int, changed: bool = False) -> None:
    """
    Run the selected solutions and merge their results into events/benchmarks.json.
    With changed, only the outdated results are run again.
    """
    # pylint: disable-next=import-outside-toplevel
    from pythonfw.scoreboard import fingerprint, solution_files

    results = load_results()
    inputs = load_inputs()
    answers = load_answers()
    if not answers:
        print("⚠️  No answer recorded by Puzzle Submitter: nothing can be verified.")
    lock = threading.Lock()

    cargo = rust_toolchain()
    if "rust" in languages and cargo is None:
        print("⚠️  No Rust toolchain found: Rust solutions are skipped.")
        languages = [language for language in languages if language != "rust"]

    tasks = []
    for year in years:
        for day in days or range(1, days_in(year) + 1):
            if day > days_in(year):
                continue
            entry = results["years"].setdefault(str(year), {}).setdefault(str(day), {})
            entry["title"] = entry.get("title") or puzzle_title(year, day)
            for language in languages:
                if not has_solution(year, day, language):
                    entry.pop(language, None)
                    continue
                code = fingerprint(solution_files(year, day, language))
                if changed and not outdated(entry.get(language), code,
                                            expected_answers(answers, year, day)):
                    continue
                tasks.append((year, day, language, code))
    if not tasks:
        print("✅ Every result is up to date.")
        save_results(results)
        return

    rust_days = [(year, day) for year, day, language, _ in tasks if language == "rust"]
    binaries = build_rust(cargo, rust_days) if rust_days else {}

    print(f"⏱️  Benchmarking {len(tasks)} solution(s), timeout {timeout:g}s, {jobs} job(s)",
          flush=True)

    def run(task):
        year, day, language, code = task
        data = puzzle_input(inputs, year, day)
        if data is None:
            run_result = {"answers": [], "time": None, "timeout": False, "error": "no input"}
        elif language == "python":
            run_result = run_python(year, day, data, timeout)
        else:
            run_result = run_rust(binaries.get(f"{year}-{day:02}"), year, day, data, timeout)
        with lock:
            expected = expected_answers(answers, year, day)
            result = grade(run_result, expected) | {"code": code}
            results["years"][str(year)][str(day)][language] = result
            save_results(results)
            print(f"  {year} day {day:>2} {language:<6} {describe(result)}", flush=True)

    with ThreadPoolExecutor(max_workers=jobs) as pool:
        list(pool.map(run, tasks))

    meta = results["meta"]
    meta["timeout"] = timeout
    meta["machine"] = machine()
    meta["date"] = datetime.date.today().isoformat()
    if "python" in languages:
        meta["python"] = platform.python_version()
    if "rust" in languages and cargo:
        meta["rust"] = subprocess.run([Path(cargo).with_name("rustc"), "--version"],
                                      capture_output=True, text=True,
                                      check=False).stdout.split()[1]
    save_results(results)


def parse_days(text: str) -> list[int]:
    """Parse '1-5', '1,3,5' or '1-3,7' into a sorted list of days."""
    days = set()
    for chunk in text.split(','):
        start, _, end = chunk.strip().partition('-')
        days.update(range(int(start), int(end or start) + 1))
    return sorted(days)


def main():
    """Entry point."""
    if len(sys.argv) == 4 and sys.argv[1] == "--child":
        python_child(int(sys.argv[2]), int(sys.argv[3]))

    parser = argparse.ArgumentParser(description="Benchmark Advent of Code solutions")
    parser.add_argument("years", type=int, nargs="*", help="years to run (default: all)")
    parser.add_argument("--days", type=parse_days, help='days to run, e.g. "1-5" or "1,3,7"')
    parser.add_argument("--lang", choices=list(LANGUAGES), action="append",
                        help="language to run (repeatable, default: all)")
    parser.add_argument("--timeout", type=float, default=300,
                        help="timeout per day in seconds (default: 300)")
    parser.add_argument("--jobs", type=int, default=1,
                        help="solutions run in parallel (default: 1, the most accurate)")
    parser.add_argument("--changed", action="store_true",
                        help="only run solutions whose code changed since their last run "
                             "(the solution or a repository module it uses), new ones, "
                             "and ones that can now be verified")
    parser.add_argument("--render", action="store_true",
                        help="only regenerate the scoreboards from the stored results")
    args = parser.parse_args()

    sys.path.insert(0, str(ROOT))
    if not args.render:
        benchmark(args.years or released_years(), args.days, args.lang or list(LANGUAGES),
                  args.timeout, args.jobs, args.changed)

    from pythonfw.scoreboard import render  # pylint: disable=import-outside-toplevel
    render()


if __name__ == '__main__':
    main()
