"""
Advent of Code - Year 2019 - Day 9
https://adventofcode.com/2019/day/9
"""

# Standard imports
from collections.abc import Iterator

# First party import
from events.year_2019.ship_computer import Program


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a comma-separated string of integers into a list of integers.
    """
    return list(map(int, puzzle_input.split(',')))


def solver(intcodes: list[int]) -> Iterator[int]:
    """
    Yields the output of running the Program with the given intcodes for input values 1 and 2.
    """
    for input_value in [1, 2]:
        yield Program(intcodes).run(input_value)
