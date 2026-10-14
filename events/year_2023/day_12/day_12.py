"""
Advent of Code - Year 2023 - Day 12
https://adventofcode.com/2023/day/12
"""

from functools import cache
from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[tuple[str, list[int]]]:
    """
    Parses the puzzle input into a list of tuples containing condition strings and
    corresponding integer patterns.
    """
    records = []
    for conditions, groups in (line.split(' ') for line in puzzle_input.splitlines()):
        groups = [int(p) for p in groups.split(',')]
        records.append((conditions, groups))
    return records


def solver(records: list[tuple[str, list[int]]]) -> Iterator[int]:
    """
    Solves both parts of the spring records problem using dynamic programming.
    """
    yield sum(count_arrangements(condition, tuple(groups))
              for condition, groups in records)
    yield sum(count_arrangements('?'.join([condition] * 5), tuple(groups * 5))
              for condition, groups in records)


def count_arrangements(condition: str, groups: tuple[int, ...]) -> int:
    """
    Count valid arrangements using dynamic programming with memoization.
    """
    return _cnt_arrgmnts(condition, groups, 0, 0, 0)


@cache
def _cnt_arrgmnts(
        condition: str,
        groups: tuple[int, ...],
        pos: int,
        group_index: int,
        group_size: int) -> int:
    """
    Dynamic programming function to count arrangements.
    """
    if pos == len(condition):
        if group_index == len(groups) and group_size == 0:
            return 1
        if group_index == len(groups) - 1 and group_size == groups[group_index]:
            return 1
        return 0

    possible_chars = {'#': '#', '.': '.', '?': '#.'}
    record = condition[pos]
    total = 0

    for c in possible_chars[record]:
        if c == '.':
            if group_size == 0:
                total += _cnt_arrgmnts(condition, groups, pos + 1, group_index, 0)
            elif group_size == groups[group_index]:
                total += _cnt_arrgmnts(condition, groups, pos + 1, group_index + 1, 0)

        elif c == '#':
            if group_index < len(groups) and group_size < groups[group_index]:
                total += _cnt_arrgmnts(condition, groups, pos + 1, group_index, group_size + 1)

    return total
