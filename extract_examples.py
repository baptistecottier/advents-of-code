#!/usr/bin/env python3
"""Extract examples for all AOC days using aocd."""

import json
import sys
from pathlib import Path

import aocd


def extract_all_examples() -> tuple[int, list[tuple[str, str]]]:
    """Extract examples for all years and days."""
    base_path = Path(__file__).parent / "events"
    total_extracted = 0
    failed_days: list[tuple[str, str]] = []

    # Extract for years 2015-2024 and days 1-25
    for year in range(2015, 2025):
        year_path = base_path / f"year_{year}"

        for day in range(1, 26):
            day_str = f"{year}/{day:02d}"
            day_path = year_path / f"day_{day:02d}"

            try:
                puzzle = aocd.get_puzzle(year=year, day=day)
                examples = puzzle.examples
                if examples:
                    # Convert examples to JSON-serializable format
                    examples_list = []
                    for ex in examples:
                        example_dict = {
                            "input_data": ex.input_data,
                            "answer_a": ex.answer_a,
                        }
                        if ex.answer_b is not None:
                            example_dict["answer_b"] = ex.answer_b
                        if ex.extra:
                            example_dict["extra"] = ex.extra
                        examples_list.append(example_dict)

                    # Save to .examples file
                    examples_file = day_path / f"day_{day:02d}.examples"
                    examples_file.parent.mkdir(parents=True, exist_ok=True)

                    with open(examples_file, "w", encoding="utf-8") as f:
                        json.dump(examples_list, f, indent=2)

                    total_extracted += 1
                    print(f"✓ {day_str}: {len(examples)} example(s)")
                else:
                    print(f"- {day_str}: no examples")
            except (ValueError, OSError) as e:
                failed_days.append((day_str, str(e)))
                print(f"✗ {day_str}: {e}")

    print(f"\n{'='*50}")
    print(f"Total examples extracted: {total_extracted}")
    if failed_days:
        print(f"Failed extractions: {len(failed_days)}")
        for day_str, error in failed_days:
            print(f"  - {day_str}: {error}")

    return total_extracted, failed_days


if __name__ == "__main__":
    total, failed = extract_all_examples()
    sys.exit(0 if not failed else 1)
