# AOCR - Advent of Code Rust Runner

A high-performance Rust CLI tool for running Advent of Code solutions across multiple years and days.

## Quick Start

### Installation

```bash
cd /Users/baptistecottier/Documents/Code/Puzzles/advents-of-code
bash scripts/install_aocr.sh
```

This will:
- Build the Rust binary in release mode
- Install it globally to `/usr/local/bin/aocr`
- Make it callable from anywhere

### Usage

```bash
# Run a single day
aocr 2024 1

# Run a day range
aocr 2024 --days 1-5

# Run specific days
aocr 2024 --days 1,3,5

# Run an entire year (shows scoreboard)
aocr 2024
aocr 2020
```

## Output

- **Single day**: Shows parsed Part 1 and Part 2 answers
- **5+ days**: Displays a scoreboard with:
  - Day completion status (✅ Complete, 🚧 Not solved, ❌ Failed)
  - Parsed answers for each part
  - Summary with success rate and star count

## Features

- ✅ Automatic project root detection (works from any directory)
- ✅ Input file caching with aocd fallback
- ✅ Output parsing for multiple formats
- ✅ Scoreboard display for multi-day runs
- ✅ Example extraction for puzzles
- ✅ Works globally from `/usr/local/bin`

## Architecture

### Modules (src/bin/)

- **aocr.rs**: Main CLI entry point, orchestrates day runs
- **args.rs**: Argument parsing (supports day ranges and lists)
- **runner.rs**: Solver execution, project root detection
- **input.rs**: Input file management with caching
- **display.rs**: Output parsing for answers
- **scoreboard.rs**: Multi-day results display
- **utils.rs**: Helper utilities

### Key Functions

**Project Root Detection** (`runner.rs`):
- Searches upward 10 levels for `events/` and `rustfw/` directories
- Falls back to hardcoded path: `/Users/baptistecottier/Documents/Code/Puzzles/advents-of-code`

**Input Loading** (`input.rs`):
- Checks local cache first: `events/year_YYYY/day_DD/day_DD.input`
- Falls back to aocd via Python if not found
- Returns empty string if input unavailable (solver can handle)

**Output Parsing** (`display.rs`):
- Supports tuple format: `("val1", "val2")`
- Supports labeled format: `Part 1: value` / `Part 2: value`
- Returns `(Option<String>, Option<String>)` for both parts

## Solver Development

To add a Rust solver for a day:

1. Create: `events/year_YYYY/day_DD/day_DD.rs`
2. Implement `main()` function
3. Read input from stdin
4. Print results as: `val1\nval2` or `Part 1: val1\nPart 2: val2`

Example:
```rust
fn main() {
    let input = std::io::read_to_string(std::io::stdin()).unwrap();
    let part1 = solve_part1(&input);
    let part2 = solve_part2(&input);
    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}
```

## Build & Test

```bash
# Build
cd rustfw
cargo build --bin aocr --release

# Test
aocr 2016 --days 1-5
aocr 2020

# Verify installation
which aocr
```

## Configuration

- **Release mode**: Always built in release mode for performance
- **Output formats**: Automatically detects and parses multiple output formats
- **Scoreboard threshold**: Shows for 5+ days, hides for 1-4 days
