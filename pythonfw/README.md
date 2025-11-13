# AOCP - Advent of Code Python Framework

A command-line tool for running Advent of Code puzzle solutions and displaying results in a scoreboard.

## Command-Line Usage

```
aocp <year> [options]
aocp <year> <days> [options]
```

### Arguments

- `<year>`: The year to run (e.g., 2015, 2023)
- `<days>`: Optional days to run (format examples below)

### Day Selection

Run a single day:
```bash
aocp 2015 1
```

Run a range of days:
```bash
aocp 2015 1-5
```

Run specific days:
```bash
aocp 2015 1,3,7,12,25
```

Run mixed ranges and specific days:
```bash
aocp 2015 1-3,7,12-15,25
```

Run all days in a year:
```bash
aocp 2015
```

### Options

- `-q, --quiet`: Show only the scoreboard (suppress solver output)
- `-t, --timeout <seconds>`: Set timeout per day (default: 60)

### Examples

```bash
# Run day 1 of 2015
aocp 2015 1

# Run days 1-10 with quiet output
aocp 2015 1-10 --quiet

# Run days 1, 5, and 10-15 with 30 second timeout
aocp 2023 1,5,10-15 --timeout 30

# Run all days of 2024 quietly
aocp 2024 --quiet
```

## Solver File Format

Each day's solution should be in a file with a `solve(data)` function that returns a tuple of answers.

Example: `events/year_2015/day_01/day_01.py`

```python
def solve(data: str) -> tuple:
    """
    Solve the day's puzzle.
    
    Args:
        data: Raw puzzle input as string
        
    Returns:
        Tuple of (part1_answer, part2_answer)
    """
    lines = data.strip().split('\n')
    
    # Part 1 logic
    part1 = 0
    for line in lines:
        part1 += int(line)
    
    # Part 2 logic
    part2 = part1 * 2
    
    return (part1, part2)
```

## Directory Structure

```
events/
├── year_2015/
│   ├── day_01/
│   │   ├── day_01.py       # Solver module with solve() function
│   │   └── day_01.input    # Puzzle input file
│   ├── day_02/
│   │   ├── day_02.py
│   │   └── day_02.input
│   └── ...
├── year_2016/
│   └── ...
└── ...
```

### Output

Default mode shows detailed output for each day. Add `--quiet` to show only the final scoreboard:

```
🎯 Running 3 day(s) for year 2015
📅 Days: 1, 2, 3

======================================================================
🏆 Scoreboard - Advent of Code 2015
======================================================================
Day    Status            Notes   │  Day    Status            Notes 
----------------------------------------------------------------------
01     ✅ Complete        ⭐⭐      │  02     ✅ Complete        ⭐⭐    
03     ✅ Complete        ⭐⭐    
======================================================================
  3/3 days completed │ 6 ⭐ (100%)

🏁 Completed 3/3 days successfully
```
