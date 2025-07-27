"""
Advent of Code - Year 2015 - Day 20
https://adventofcode.com/2015/day/20
"""

from math import sqrt


def solver(puzzle_input: str) -> tuple[int, int]:
    """
    Solves the puzzle by finding the lowest house number that receives at least the target number
    of presents.

    Args:
        puzzle_input (str): The target number of presents as a string.

    Returns:
        tuple[int, int]: A tuple containing the lowest house number for part 1 and part 2.

    Examples:
        >>> solver("150")
        (8, 6)
    """
    target = int(puzzle_input)
    return find_lucky_house(target, 10), find_lucky_house(target, 11, 50)


def find_lucky_house(target: int, multiplier: int, max_houses_per_elf: int = -1) -> int:
    """
    Finds the lowest house number that receives at least the target number of presents.

    Args:
        target (int): The minimum number of presents required.
        multiplier (int): The number of presents each elf delivers per house.
        max_houses_per_elf (int, optional): The maximum number of houses each elf visits. Defaults
                                            to -1 (no limit).

    Returns:
        int: The lowest house number meeting the target.

    Examples:
        >>> find_lucky_house(29000000, 10)
        665280
    """
    n = 210
    while bounded_divisors_sum(n, max_houses_per_elf) < (target // multiplier):
        n += 210
    return n


def bounded_divisors_sum(n: int, bound: int) -> int:
    """
    Calculate the sum of divisors and their corresponding quotients for a given number.

    If bound is -1, it defaults to the square root of n. Otherwise, it considers
    divisors up to the specified bound.

    Args:
        n: The number to find divisors for
        bound: Upper limit for divisors to consider (-1 for sqrt(n))

    Returns:
        Sum of all divisors and their corresponding quotients

    Examples:
        >>> bounded_divisors_sum(12, -1)
        28  # (1 + 12) + (2 + 6) + (3 + 4)
        >>> bounded_divisors_sum(12, 2)
        21  # (1 + 12) + (2 + 6)
    """
    if bound == -1:
        bound = int(sqrt(n))
    return sum(k + (n // k) for k in range(1, 1 + bound) if n % k == 0)
