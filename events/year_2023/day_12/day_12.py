"""
Advent of Code - Year 2023 - Day 12
https://adventofcode.com/2023/day/12
"""

from collections.abc import Iterator
from itertools import product


def preprocessing(puzzle_input: str) -> list[tuple[str, list[int]]]:
    """
    Parses the puzzle input into a sorted list of tuples containing condition strings and
    corresponding integer patterns.
    """
    records = []
    for conditions, pattern in (line.split(' ') for line in puzzle_input.splitlines()):
        pattern = [int(p) for p in pattern.split(',')]
        records.append((conditions, pattern))
    return sorted(records, key=lambda x: len(x[0]))


def solver(records: list[tuple[str, list[int]]]) -> Iterator[int]:
    """
    Yields the result of testing the provided records using the test function.
    """
    yield test(records)
    # yield test(records, 4) # Theoritically correct


def test(records: list[tuple[str, list[int]]], rep: int = 0) -> int:
    """
    Counts the number of valid arrangements of '#' and '.' in the given records that match the
    specified patterns, optionally repeating them.
    """
    cnt = 0
    for condition, pattern in records:
        condition += f'?{condition}' * rep
        pattern += rep * pattern
        nb_jokers = condition.count('?')
        k = condition.count('#')
        for jokers in product(['#', '.'], repeat=nb_jokers):
            if jokers.count('#') != sum(pattern) - k:
                continue
            c = condition
            j = list(jokers)
            while j:
                c = c.replace('?', j.pop(), 1)
            if c.count('#') == sum(pattern):
                test_value = [item.count('#') for item in c.split('.') if item != '']
                if test_value == pattern:
                    cnt += 1
    return cnt
