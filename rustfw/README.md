# AOCR - Advent of Code Rust Runner

A high-performance Rust CLI tool for running Advent of Code solutions.

## Installation

```bash
bash scripts/install_aocr.sh
```

This builds the binary in release mode and installs it globally to `/usr/local/bin/aocr`.

## Command-Line Usage

```
aocr <year> [options]
aocr <year> <days> [options]
```

### Arguments

- `<year>`: The year to run (e.g., 2015, 2023)
- `<days>`: Optional days to run (format examples below)

### Day Selection

Run a single day:
```bash
aocr 2015 1
```

Run a range of days:
```bash
aocr 2015 1-5
```

Run specific days:
```bash
aocr 2015 1,3,7,12,25
```

Run mixed ranges and specific days:
```bash
aocr 2015 1-3,7,12-15,25
```

Run all days in a year (shows scoreboard):
```bash
aocr 2015
```

## 📊 Progress Summary

| Year | Progress |
| :-: | :- |
| 2024 | ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 22/50 |
| 2023 | ⭐⭐⭐⭐⭐⭐ 12/50 |
| 2022 | ⭐⭐⭐⭐⭐⭐⭐⭐⭐ 18/50 |
| 2021 | ⭐⭐⭐⭐ 8/50 |
| 2020 | ⭐⭐⭐⭐⭐⭐⭐⭐ 16/50 |
| 2019 | ⭐ 2/50 |
| 2018 | ⭐⭐⭐⭐ 8/50 |
| 2017 | ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 24/50 |
| 2016 | ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 28/50 |
| 2015 | ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 44/50 |

**Total: 182/550 ⭐ (33%)**

## Solver File Format

Create a Rust solver at `events/year_YYYY/day_DD/day_DD.rs` with a `main()` function that reads input from stdin and prints results.

Example: `events/year_2015/day_01/day_01.rs`

```rust
fn main() {
    let input = std::io::read_to_string(std::io::stdin()).unwrap();
    
    // Part 1 logic
    let part1: i32 = input.lines().map(|l| l.parse::<i32>().unwrap()).sum();
    
    // Part 2 logic
    let part2 = part1 * 2;
    
    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}
```

You can also output results on separate lines without labels:

```rust
println!("{}", part1);
println!("{}", part2);
```

## Directory Structure

```
events/
├── year_2015/
│   ├── day_01/
│   │   ├── day_01.rs       # Solver with main() function
│   │   └── day_01.input    # Puzzle input file
│   ├── day_02/
│   │   ├── day_02.rs
│   │   └── day_02.input
│   └── ...
├── year_2016/
│   └── ...
└── ...
```

## Output

Single day output shows the parsed answers. Running 5+ days displays a scoreboard:

```
======================================================================
🏆 Scoreboard - Advent of Code 2015
======================================================================
Day    Status            │  Day    Status            
----------------------------------------------------------------------
01     ✅ Complete        │  02     ✅ Complete       
03     ✅ Complete        │  04     ✅ Complete       
======================================================================
4/4 days completed (100%)
```
