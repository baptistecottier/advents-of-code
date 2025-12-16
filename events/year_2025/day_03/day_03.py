"""
Advent of Code - Year 2025 - Day 3
https://adventofcode.com/2025/day/3
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Generate the set of banks given initial input
    """
    return [list(map(int, line)) for line in puzzle_input.splitlines()]


def solver(banks: list[list[int]]) -> Iterator[int]:
    """
    Given a set of banks, compute and sum the largest possible joltage for each bank, given two
    possible amount of batteries to turn on: 2 and 12
    """
    for size in (2, 12):
        yield sum(compute_largest_joltage(bank, size) for bank in banks)


def compute_largest_joltage(bank: list[int], size: int) -> int:
    """
    Given a bank, compute the largest possible joltage.
    """
    if len(bank) < size:
        raise ValueError("Not enought batteries")

    start = 0
    jolt = 0
    for k in range(len(bank) - size, len(bank), 1):
        digit = max(bank[start:k + 1])
        start = start + bank[start:].index(digit) + 1
        jolt = 10 * jolt + digit
    return jolt
