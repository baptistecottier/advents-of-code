#!/usr/bin/env python3
"""
Smart completion helpers for aocp and aocr - provides dynamic completions based on available files.
"""

import os
from pathlib import Path


def get_available_years():
    """Get years that have solution directories."""
    years = []
    events_dir = Path("./events")
    if events_dir.exists():
        for year_dir in events_dir.iterdir():
            if year_dir.is_dir() and year_dir.name.startswith("year_"):
                try:
                    year = int(year_dir.name.split("_")[1])
                    years.append(year)
                except (IndexError, ValueError):
                    continue
    
    # Add common years even if directories don't exist
    for year in range(2015, 2026):
        if year not in years:
            years.append(year)
    
    return sorted(years)


def get_available_days(year):
    """Get days that have solution files for a given year."""
    days = []
    year_dir = Path(f"./events/year_{year}")
    if year_dir.exists():
        for day_dir in year_dir.iterdir():
            if day_dir.is_dir() and day_dir.name.startswith("day_"):
                try:
                    day = int(day_dir.name.split("_")[1])
                    days.append(day)
                except (IndexError, ValueError):
                    continue
    
    # Add all days 1-25 if none found
    if not days:
        days = list(range(1, 26))
    
    return sorted(set(days))


def get_solution_files(year, day=None):
    """Get available solution files for a year/day."""
    files = []
    
    if day:
        day_str = f"{day:02d}"
        day_dir = Path(f"./events/year_{year}/day_{day_str}")
        if day_dir.exists():
            for ext in ['.py', '.rs']:
                solution_file = day_dir / f"day_{day_str}{ext}"
                if solution_file.exists():
                    files.append(str(solution_file))
    else:
        year_dir = Path(f"./events/year_{year}")
        if year_dir.exists():
            for day_dir in year_dir.iterdir():
                if day_dir.is_dir() and day_dir.name.startswith("day_"):
                    for ext in ['.py', '.rs']:
                        solution_files = list(day_dir.glob(f"day_*.{ext[1:]}"))
                        files.extend([str(f) for f in solution_files])
    
    return files


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python completion_helpers.py <command>")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "years":
        years = get_available_years()
        print(" ".join(map(str, years)))
    
    elif command == "days" and len(sys.argv) >= 3:
        try:
            year = int(sys.argv[2])
            days = get_available_days(year)
            print(" ".join(map(str, days)))
        except ValueError:
            print(" ".join(map(str, range(1, 26))))
    
    elif command == "files" and len(sys.argv) >= 3:
        try:
            year = int(sys.argv[2])
            day = int(sys.argv[3]) if len(sys.argv) >= 4 else None
            files = get_solution_files(year, day)
            print(" ".join(files))
        except ValueError:
            pass
    
    else:
        print(" ".join(map(str, range(1, 26))))  # Default: all days