"""
Advent of Code - Year 2018 - Day 1
https://adventofcode.com/2018/day/1
"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Convert puzzle input string to a list of integer frequency changes.
    """
    changes = list(map(int, puzzle_input.replace(', ', '\n').splitlines()))
    return changes


def solver(changes: list[int]) -> tuple[int, int]:
    """
    Solve the frequency puzzle by finding the sum of all changes and the first repeated frequency.

    Args:
        changes: List of integer frequency changes.

    Returns:
        tuple: (total_sum, first_repeated_frequency)

    Raises:
        ValueError: If the number of unique frequencies exceeds 1 million.
    """
    frequencies = set()
    frequency = 0
    index = 0

    while frequency not in frequencies:
        if len(frequencies) > 1_000_000:
            raise ValueError("Too much frequencies to deal with. Abort")
        frequencies.add(frequency)
        frequency += changes[index]
        index = (index + 1) % len(changes)

    return sum(changes), frequency
