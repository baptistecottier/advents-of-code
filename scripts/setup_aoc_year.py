#!/usr/bin/env python3
"""
Advanced Advent of Code Year Setup Script
Provides more flexibility and features than the bash version.

Usage: python3 setup_aoc_year.py <year> [options]
"""

import argparse
import os
import sys
from pathlib import Path
import re
from typing import Optional
import subprocess
import tempfile


class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color


def print_colored(message: str, color: str = Colors.NC) -> None:
    """Print a colored message."""
    print(f"{color}{message}{Colors.NC}")


def print_info(message: str) -> None:
    print_colored(f"[INFO] {message}", Colors.BLUE)


def print_success(message: str) -> None:
    print_colored(f"[SUCCESS] {message}", Colors.GREEN)


def print_warning(message: str) -> None:
    print_colored(f"[WARNING] {message}", Colors.YELLOW)


def print_error(message: str) -> None:
    print_colored(f"[ERROR] {message}", Colors.RED)


def create_rust_template(day: int) -> str:
    """Generate Rust template content."""
    return f"""aoc::main!();

fn preprocessing(input: &str) -> Vec<&str> {{
    input.lines().collect()
}}

fn part_1(data: Vec<&str>) -> usize {{
    // TODO: Implement part 1
    0
}}

fn part_2(data: Vec<&str>) -> usize {{
    // TODO: Implement part 2
    0
}}
"""


def create_python_template(year: int, day: int) -> str:
    """Generate Python template content."""
    return f'''"""
Advent of Code - Year {year} - Day {day}
https://adventofcode.com/{year}/day/{day}
"""


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Processes the puzzle input into a suitable data structure.
    """
    return puzzle_input.strip().split('\\n')


def solver(data: list[str]) -> tuple[int, int]:
    """
    Solves both parts of the puzzle.
    Returns a tuple (part1_result, part2_result).
    """
    # TODO: Implement part 1
    part1 = 0
    
    # TODO: Implement part 2  
    part2 = 0
    
    return part1, part2
'''


def create_markdown_template(year: int, day: int, title: str = "TBD") -> str:
    """Generate Markdown template content."""
    return f"""# Day {day}: {title}

## Part 1

TODO: Describe part 1

## Part 2

TODO: Describe part 2

## Notes

- Solution approach:
- Time complexity:
- Space complexity:
"""


def setup_aoc_year(
    year: int,
    num_days: int = 25,
    force: bool = False,
    dry_run: bool = False,
    emoji: str = "🎉",
    create_md_content: bool = False
) -> None:
    """Set up Advent of Code year structure."""
    
    # Find project root
    script_dir = Path(__file__).parent.absolute()
    project_root = script_dir
    
    # Look for events directory (go up directories if needed)
    while project_root != project_root.parent:
        if (project_root / "events").exists():
            break
        project_root = project_root.parent
    else:
        print_error("Could not find project root with 'events' directory")
        sys.exit(1)
    
    events_dir = project_root / "events"
    year_dir = events_dir / f"year_{year}"
    rustfw_dir = project_root / "rustfw"
    
    print_info(f"Setting up Advent of Code {year} with {num_days} days...")
    if dry_run:
        print_warning("DRY RUN MODE - No files will be created")
    
    # Check if year already exists
    if year_dir.exists() and not force:
        print_error(f"Year {year} already exists at {year_dir}")
        print_info("Use --force to overwrite or choose a different year")
        sys.exit(1)
    
    if dry_run:
        print_info(f"Would create: {year_dir}")
        print_info(f"Would create {num_days} day directories with files")
        return
    
    # Remove existing if force is used
    if year_dir.exists() and force:
        print_warning(f"Removing existing {year_dir}")
        import shutil
        shutil.rmtree(year_dir)
    
    # Create year directory
    year_dir.mkdir(parents=True, exist_ok=True)
    print_success(f"Created year directory: {year_dir}")
    
    # Create day directories and files
    for day in range(1, num_days + 1):
        day_formatted = f"{day:02d}"
        day_dir = year_dir / f"day_{day_formatted}"
        
        print_info(f"Creating day {day_formatted}...")
        day_dir.mkdir(exist_ok=True)
        
        # Create Rust file
        rust_file = day_dir / f"day_{day_formatted}.rs"
        rust_file.write_text(create_rust_template(day))
        
        # Create Python file
        python_file = day_dir / f"day_{day_formatted}.py"
        python_file.write_text(create_python_template(year, day))
        
        # Create Markdown file
        md_file = day_dir / f"day_{day_formatted}.md"
        if create_md_content:
            md_file.write_text(create_markdown_template(year, day))
        else:
            md_file.touch()
        
        # Create input file
        input_file = day_dir / f"day_{day_formatted}.input"
        input_file.touch()
    
    print_success(f"Created {num_days} day directories with files")
    
    # Update Cargo.toml
    cargo_toml = rustfw_dir / "Cargo.toml"
    if cargo_toml.exists():
        print_info("Updating Cargo.toml...")
        
        with open(cargo_toml, 'a') as f:
            for day in range(1, num_days + 1):
                day_formatted = f"{day:02d}"
                f.write(f'''

[[bin]]
name = "{year}-{day_formatted}"
path = "../events/year_{year}/day_{day_formatted}/day_{day_formatted}.rs"
''')
        
        print_success(f"Added {num_days} binary entries to Cargo.toml")
    else:
        print_warning(f"Cargo.toml not found at {cargo_toml}")
    
    # Update README.md
    readme = project_root / "README.md"
    if readme.exists():
        print_info("Updating README.md...")
        
        content = readme.read_text()
        
        # Add to summary table
        summary_pattern = r'(Year\s+\|\s+🐍\s+\|\s+🦀\s+\|\s*\n:---:\s+\|\s+:---:\s+\|\s+:--:\s+\|)'
        summary_replacement = rf'\1\n[{year}](#{year}) | 0      | 0'
        content = re.sub(summary_pattern, summary_replacement, content)
        
        # Generate detailed section
        detailed_section = f'''<details>
    <summary> 
    <a id="{year}"><h2>{year} {emoji}</h2></a>
    </summary>

| Day | Title                     | Python | Rust |
| :-: | :------------------------ | :----: | :--: |
'''
        
        for day in range(1, num_days + 1):
            day_formatted = f"{day:02d}"
            detailed_section += f"| {day_formatted} | [TBD](events/year_{year}/day_{day_formatted}/day_{day_formatted}.md) |  |  |\n"
        
        detailed_section += "\n</details>\n\n"
        
        # Add detailed section after "## ⭐ Yearly detailed scores"
        scores_pattern = r'(## ⭐ Yearly detailed scores\s*\n)'
        scores_replacement = rf'\1\n{detailed_section}'
        content = re.sub(scores_pattern, scores_replacement, content)
        
        readme.write_text(content)
        print_success("Updated README.md")
    else:
        print_warning(f"README.md not found at {readme}")
    
    # Test compilation
    print_info("Testing Rust compilation...")
    try:
        result = subprocess.run(
            ["cargo", "check", "--bin", f"{year}-01"],
            cwd=rustfw_dir,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print_success("Rust compilation test passed")
        else:
            print_warning("Rust compilation test failed")
    except FileNotFoundError:
        print_warning("Cargo not found - skipping compilation test")
    
    # Test Python import
    print_info("Testing Python import...")
    try:
        result = subprocess.run(
            ["python3", "-c", f"import day_01; print('Python import successful')"],
            cwd=year_dir / "day_01",
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print_success("Python import test passed")
        else:
            print_warning("Python import test failed")
    except Exception:
        print_warning("Python test failed")
    
    # Final summary
    print_success(f"🎄 Advent of Code {year} setup complete! 🎄")
    print_info("")
    print_info("What was created:")
    print_info(f"  📁 {num_days} day directories in events/year_{year}/")
    print_info(f"  🦀 {num_days} Rust template files (.rs)")
    print_info(f"  🐍 {num_days} Python template files (.py)")
    print_info(f"  📝 {num_days} Markdown files (.md)")
    print_info(f"  📄 {num_days} Input files (.input)")
    print_info(f"  ⚙️  Updated Cargo.toml with {num_days} binary entries")
    print_info(f"  📚 Updated README.md with {year} section")
    print_info("")
    print_info("Usage examples:")
    print_info(f"  Rust: cargo run --bin {year}-01")
    print_info(f"  Python: cd events/year_{year}/day_01 && python3 day_01.py")
    print_info("")
    print_info(f"Ready for December {year}! 🎅")


def main():
    parser = argparse.ArgumentParser(
        description="Set up Advent of Code year structure",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 setup_aoc_year.py 2026                    # Standard 25 days
  python3 setup_aoc_year.py 2026 --days 12          # Only 12 days
  python3 setup_aoc_year.py 2026 --force            # Overwrite existing
  python3 setup_aoc_year.py 2026 --dry-run          # Preview changes
  python3 setup_aoc_year.py 2026 --emoji "🚀"       # Custom emoji
        """
    )
    
    parser.add_argument('year', type=int, help='Year to set up (e.g., 2026)')
    parser.add_argument('--days', type=int, default=25, 
                       help='Number of days to create (default: 25)')
    parser.add_argument('--force', action='store_true',
                       help='Overwrite existing year directory')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be created without creating files')
    parser.add_argument('--emoji', default='🎉',
                       help='Emoji for the year section (default: 🎉)')
    parser.add_argument('--create-md-content', action='store_true',
                       help='Create markdown files with template content')
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.year < 2015 or args.year > 2050:
        print_error(f"Invalid year: {args.year} (must be between 2015-2050)")
        sys.exit(1)
    
    if args.days < 1 or args.days > 25:
        print_error(f"Invalid number of days: {args.days} (must be between 1-25)")
        sys.exit(1)
    
    try:
        setup_aoc_year(
            year=args.year,
            num_days=args.days,
            force=args.force,
            dry_run=args.dry_run,
            emoji=args.emoji,
            create_md_content=args.create_md_content
        )
    except KeyboardInterrupt:
        print_error("\nAborted by user")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()