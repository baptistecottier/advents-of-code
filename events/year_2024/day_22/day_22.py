"""
Advent of Code - Year 2024 - Day 22
https://adventofcode.com/2024/day/22
"""

from collections import defaultdict


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts the puzzle input string into a list of integers, one per line.
    """
    return list(map(int, puzzle_input.splitlines()))


def solver(secret_numbers: list[int]) -> tuple[int, int]:
    """
    Processes a list of secret numbers, evolving each to generate sequences and returns the sum of
    final numbers and the maximum bananas stock.
    """
    sequences = {}
    sum_generated_numbers = 0
    for secret_id, secret_number in enumerate(secret_numbers):
        a, b, c, d = 0, 0, 0, 0
        for rep in range(2_000):
            (a, b, c) = (b, c, d)
            secret_number, d = evolve(secret_number)
            if rep > 2:
                if (secret_id, a, b, c, d) not in sequences:
                    sequences[(secret_id, a, b, c, d)] = secret_number % 10
        sum_generated_numbers += secret_number

    bananas_stock = defaultdict(int)
    for (_, a, b, c, d), bananas in sequences.items():
        bananas_stock[(a, b, c, d)] += bananas

    return sum_generated_numbers, max(bananas_stock.values())


def evolve(n: int) -> tuple[int, int]:
    """
    Evolves the input integer n through a series of mix_and_prune transformations and returns the
    final result and the difference of their last digits.
    """
    temp = mix_and_prune(n << 6, n)
    temp = mix_and_prune(temp >> 5, temp)
    temp = mix_and_prune(temp << 11, temp)
    return temp, (temp % 10) - (n % 10)


def mix_and_prune(a: int, b: int) -> int:
    """
    Returns the bitwise XOR of a and b, masked to the lowest 24 bits.
    """
    return (a ^ b) & ((1 << 24) - 1)
