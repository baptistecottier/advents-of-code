# 🎄 Advent of Code Year Setup Script

Automated script to set up the complete project structure for any Advent of Code year.

## 🚀 Quick Start

```bash
# Standard setup (25 days)
python3 setup_aoc_year.py 2026

# Custom number of days  
python3 setup_aoc_year.py 2026 --days 12

# Preview first (recommended)
python3 setup_aoc_year.py 2026 --dry-run

# With custom emoji
python3 setup_aoc_year.py 2026 --emoji "🚀"
```

## 📋 What Gets Created

For each year, both scripts create:

### 📁 **Directory Structure**
```
events/year_YYYY/
├── day_01/
│   ├── day_01.rs      # Rust solution template
│   ├── day_01.py      # Python solution template  
│   ├── day_01.md      # Puzzle description
│   └── day_01.input   # Input data file
├── day_02/
│   └── ... (same structure)
└── day_XX/
    └── ... (up to specified number of days)
```

### ⚙️ **Configuration Updates**
- **Cargo.toml**: Adds binary entries for all Rust solutions
- **README.md**: Adds year to summary table and detailed sections

### 🧪 **Validation**
- Tests Rust compilation with `cargo check`
- Tests Python import functionality
- Provides usage examples

## 📖 Usage Examples
```bash
# Standard setup (25 days)
python3 setup_aoc_year.py 2026

# Preview without creating files (recommended first step)
python3 setup_aoc_year.py 2026 --dry-run

# Only 12 days with custom emoji
python3 setup_aoc_year.py 2026 --days 12 --emoji "🚀"

# Overwrite existing year (be careful!)
python3 setup_aoc_year.py 2025 --force

# Create with rich markdown templates
python3 setup_aoc_year.py 2026 --create-md-content

# Show all options
python3 setup_aoc_year.py --help
```

## 🎯 Key Features

- ✅ **Dry Run Mode** - Preview changes before creating files
- ✅ **Custom Days** - Create 1-25 days (perfect for special years)  
- ✅ **Custom Emojis** - Match your personal style (🚀🎪🌟⚡)
- ✅ **Force Overwrite** - Clean automation without prompts
- ✅ **Rich Templates** - Optional detailed markdown content
- ✅ **Comprehensive Validation** - Tests both Rust and Python
- ✅ **Excellent Error Handling** - Clear, colored output
- ✅ **Future-Proof** - Easy to extend with new features

## 🛠 Template Contents

### Rust Template (`day_XX.rs`)
```rust
aoc::main!();

fn preprocessing(input: &str) -> Vec<&str> {
    input.lines().collect()
}

fn part_1(data: Vec<&str>) -> usize {
    // TODO: Implement part 1
    0
}

fn part_2(data: Vec<&str>) -> usize {
    // TODO: Implement part 2
    0
}
```

### Python Template (`day_XX.py`)
```python
"""
Advent of Code - Year YYYY - Day X
https://adventofcode.com/YYYY/day/X
"""

def preprocessing(puzzle_input: str) -> list[str]:
    """
    Processes the puzzle input into a suitable data structure.
    """
    return puzzle_input.strip().split('\n')

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
```

## 🎄 Ready to Use!

After running either script:

```bash
# Run Rust solution
cargo run --bin 2026-01

# Run Python solution  
cd events/year_2026/day_01
python3 day_01.py

# Check compilation
cargo check --bin 2026-01
```

The script is designed to be **idempotent** and **safe** - it includes comprehensive validation, error handling, and dry-run mode to preview changes.

## 🏃‍♂️ Running Solutions with `aocp`

The improved `aocp` script now supports flexible command-line arguments:

### Basic Usage
```bash
# Run a specific day
./aocp 2024 1

# Run with examples first  
./aocp 2024 1 --examples

# Run all days of a year
./aocp 2024

# Run specific days
./aocp 2024 --days 1,3,5

# Run a range of days
./aocp 2024 --days 1-5
```

### Advanced Options
```bash
# Use remote input only (skip local files)
./aocp 2024 1 --no-local

# Test examples with detailed output
./aocp 2024 1 --examples-verbose

# Force run even if examples fail
./aocp 2024 1 --examples --force

# Show help
./aocp --help
```

### Input File Priority
1. **Local files**: `events/year_YYYY/day_DD/day_DD.input` (if exists and not empty)
2. **Remote**: Downloads from Advent of Code automatically

**Perfect for setting up any future Advent of Code year with zero manual work!** 🎅