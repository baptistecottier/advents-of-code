"""
Advent of Code - Year 2017 - Day 5
https://adventofcode.com/2017/day/5
"""

from collections.abc import Callable


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts puzzle input as a list of int

    Example:
        >>> preprocessing("0\n3\n0\n1\n-3)
        [0, 3, 0, 1, -3]
    """
    return [int(item) for item in puzzle_input.split()]


def solver(offsets: list[int]) -> tuple[int, int]:
    """
    Calculate steps needed to exit a list of offsets using different increment rules.

    Yields:
        int: Two values representing steps needed to exit:
            1. Using simple increment rule (always +1)
            2. Using complex increment rule (+1 if offset < 3, else -1)

    Args:
        offsets (list): List of integers representing jump offsets

    Example:
        >>> list(solver([0, 3, 0, 1, -3]))
        [5, 10]
    """
    return (steps_to_exit(offsets.copy(), lambda _: 1),
            steps_to_exit(offsets, lambda x: 1 if x < 3 else -1))


def steps_to_exit(offsets: list[int], func: Callable) -> int:
    """
    Calculate steps needed to exit a list of jump offsets.

    Args:
        offsets: List of integer jump offsets.
        func: Function to modify each offset after jumping from it.

    Returns:
        int: Number of steps taken to exit the list.
    """
    steps = 0
    pos = 0
    while 0 <= pos < len(offsets):
        offsets[pos], pos = offsets[pos] + func(offsets[pos]), pos + offsets[pos]
        steps += 1
    return steps
