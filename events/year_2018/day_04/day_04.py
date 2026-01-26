"""
Advent of Code - Year 2018 - Day 4
https://adventofcode.com/2018/day/4
"""

# Standard import
from itertools import product

# Third-party imports
from parse import parse, Result


def preprocessing(puzzle_input: str) -> dict[int, list[int]]:
    """
    Parse and sort timestamped records from puzzle input, extracting date and time components.
    """
    guard_id = 0
    records = []
    for line in sorted(puzzle_input.splitlines()):
        result = parse("[{:d}-{:d}-{:d} {:d}:{:d}]{}", line)
        if isinstance(result, Result):
            if "Guard" in result[5]:
                guard_id = int(result[5].split(' ')[2][1:])
                continue
            records.append((result[4], guard_id))
    timesheet = get_timesheet(records)
    return timesheet


def solver(timesheet: dict[int, list[int]]) -> tuple[int, int]:
    """
    Solve guard duty puzzle using two strategies to find optimal guard-minute combinations.
    """
    lazy_guard = max(timesheet.keys(),
                     key=lambda g: sum(timesheet[g]))
    strategy_1 = lazy_guard * timesheet[lazy_guard].index(max(timesheet[lazy_guard]))

    lazy_guard, minute = max(product(timesheet.keys(), range(60)),
                             key=lambda gm: timesheet[gm[0]][gm[1]])
    strategy_2 = lazy_guard * minute
    return strategy_1, strategy_2


def get_timesheet(records: list[tuple[int, ...]]) -> dict[int, list[int]]:
    """
    Generate a timesheet tracking sleep minutes for guards from shift records.
    """
    timesheet = {}
    for i in range(0, len(records), 2):
        (start_m, guard_id) = records[i]
        (end_m, guard_id) = records[i+1]
        if guard_id not in timesheet:
            timesheet[guard_id] = [0 for _ in range(60)]
        for j in range(start_m, end_m):
            timesheet[guard_id][j] += 1
    return timesheet
