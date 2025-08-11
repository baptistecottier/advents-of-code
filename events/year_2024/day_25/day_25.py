"""
Advent of Code - Year 2024 - Day 25
https://adventofcode.com/2024/day/25
"""

from itertools import product


def preprocessing(puzzle_input: str) -> tuple[list[list[int]], list[list[int]]]:
    """
    Processes the puzzle input into lists of lock and key block patterns based on '#' character
    positions.
    """
    locks = []
    keys = []

    blocks = puzzle_input.split('\n\n')
    for raw_block in blocks:
        raw_block = raw_block.replace('\n', '')
        block = [-1, -1, -1, -1, -1]
        for i, c in enumerate(raw_block):
            if c == '#':
                block[i % 5] += 1
        if raw_block.startswith("#####"):
            if block not in locks:
                locks.append(block)
        elif block not in keys:
            keys.append(block)
    return locks, keys


def solver(locks: list[list[int]], keys: list[list[int]]) -> tuple[int]:
    """
    Counts the number of lock-key pairs where the sum of corresponding elements does not exceed 5
    for all positions.
    """
    pairs = 0
    for lock, key in product(locks, keys):
        if all((ll + kk) <= 5 for ll, kk in zip(lock, key)):
            pairs += 1
    return (pairs,)
