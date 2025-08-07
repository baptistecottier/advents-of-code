"""
Advent of Code - Year 2021 - Day 1
https://adventofcode.com/2021/day/1
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a multiline string of numbers into a list of integers.
    """
    return list(map(int, puzzle_input.splitlines()))


def solver(measurements: list[int]) -> Iterator[int]:
    """
    Yields the count of times a measurement increases compared to the previous measurement, for
    window sizes of 1 and 3.
    """
    for size in [1, 3]:
        cnt = 0
        for a, b in zip(measurements, measurements[size:]):
            if a < b:
                cnt += 1
        yield cnt
