"""
Advent of Code - Year 2024 - Day 11
https://adventofcode.com/2024/day/11
"""

from collections import defaultdict
from collections.abc import Iterator
from math import log10


def preprocessing(puzzle_input: str) -> dict[int, int]:
    """
    Processes the puzzle input string and returns a dictionary mapping each stone value to its
    count.
    """
    stones = defaultdict(int)
    for stone in puzzle_input.split():
        stones[int(stone)] += 1
    return stones


def solver(stones: dict[int, int]) -> Iterator[int]:
    """
    Yields the sum of stone values after 25 and 75 iterations of the blink function.
    """
    for i in range(1, 76):
        stones = blink(stones)
        if i in [25, 75]:
            yield sum(stones.values())


def blink(stones: dict[int, int], times: int = 1) -> dict[int, int]:
    """
    Transforms a dictionary of stones according to specific rules for a given number of times.
    """
    new_stones = defaultdict(int)
    for _ in range(times):
        new_stones = defaultdict(int)
        for stone, n in stones.items():
            if stone == 0:
                new_stones[1] += n
            elif (log := int(log10(stone))) % 2 == 1:
                new_stones[stone // pow(10, log // 2 + 1)] += n
                new_stones[stone % pow(10, log // 2 + 1)] += n
            else:
                new_stones[2024 * stone] += n
        stones = new_stones
        new_stones = defaultdict(int)
    return stones
