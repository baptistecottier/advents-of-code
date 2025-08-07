"""
Advent of Code - Year 2021 - Day 6
https://adventofcode.com/2021/day/6
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> dict[int, int]:
    """
    Converts the puzzle input string into a dictionary mapping each integer from 0 to 8 to its
    count in the input.
    """
    return {n: puzzle_input.count(str(n)) for n in range(9)}


def solver(lanternfishes: dict[int, int]) -> Iterator[int]:
    """
    Simulates lanternfish population growth over 256 days, yielding the total count at day 80
    and at the end.
    """
    for day in range(256):
        if day == 80:
            yield sum(lanternfishes.values())
        lanternfishes[9] = lanternfishes[0]
        lanternfishes[7] += lanternfishes[0]
        lanternfishes = {n: lanternfishes[n + 1] for n in range(9)}
    yield sum(lanternfishes.values())
