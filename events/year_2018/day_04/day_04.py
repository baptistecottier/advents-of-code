"""
Advent of Code - Year 2018 - Day 4
https://adventofcode.com/2018/day/4
"""

# Standard import
from itertools import product

# Third-party imports
from parse import parse, Result


def preprocessing(puzzle_input: str) -> list[list[int]]:
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
            else:
                guard_id = -1
            records.append(result[:5] + (guard_id,))
    return records


def solver(records: list[list[int]]) -> tuple[int, int]:
    """
    Solve guard duty puzzle using two strategies to find optimal guard-minute combinations.
    """
    timesheet = get_timesheet(records)

    lazy_guard = max(timesheet.keys(),
                     key=lambda g: sum(timesheet[g]))
    strategy_1 = lazy_guard * timesheet[lazy_guard].index(max(timesheet[lazy_guard]))

    lazy_guard, minute = max(product(timesheet.keys(), range(60)),
                             key=lambda gm: timesheet[gm[0]][gm[1]])
    strategy_2 = lazy_guard * minute
    return strategy_1, strategy_2


def get_timesheet(records) -> dict[int, list[int]]:
    """
    Generate a timesheet tracking sleep minutes for guards from shift records.
    """
    timesheet = {}
    guard = 0

    for i, record in enumerate(records[:-1]):
        if record[-1] == -1:
            for j in range(record[-2], records[i+1][-2]):
                timesheet[guard][j] += 1
        else:
            guard = record[-1]
            if guard not in timesheet:
                timesheet[guard] = [0 for _ in range(60)]
    return timesheet
