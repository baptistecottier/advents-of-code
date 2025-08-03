"""
Advent of Code - Year 2020 - Day 1
https://adventofcode.com/2020/day/1
"""

from collections.abc import Iterator
from itertools import product
from math import prod


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a multiline string of numbers into a list of integers.
    """
    return list(map(int, puzzle_input.splitlines()))


def solver(expenses: list[int]) -> Iterator[int]:
    """
    Yields the result of finding entries in the expenses list that sum to a target value for each
    specified number of entries (2 and 3).
    """
    for n_entries in [2, 3]:
        yield find_entries(expenses, n_entries)


def find_entries(expenses: list[int], n_entries: int) -> int:
    """
    Finds the product of the first combination of 'n_entries' numbers from 'expenses' that sum to
    2020, or raises a ValueError if none is found.
    """
    for c in product(expenses, repeat=n_entries):
        if sum(c) == 2020:
            return prod(c)
    raise ValueError("No combination summing to 2020 found!")
