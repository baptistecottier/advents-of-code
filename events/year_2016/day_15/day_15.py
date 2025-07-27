"""
Advent of Code - Year 2016 - Day 15
https://adventofcode.com/2016/day/15
"""

# Standard imports
from re import findall

# First-party imports
from pythonfw.functions import chinese_remainder


def preprocessing(puzzle_input: str) -> set[tuple[int, int]]:
    """
    Parse puzzle input to extract disc equations for timing calculations.

    Args:
        puzzle_input: Raw puzzle input containing disc parameters

    Returns:
        Set of tuples representing disc equations as (offset, period) pairs
    """
    values = list(int(item) for item in findall(r"[0-9]+", puzzle_input))
    equations = set()
    while values:
        ta, _, tn, d = values.pop(), values.pop(), values.pop(), values.pop()
        equations.add((-(ta + d), tn))
    return equations


def solver(equations: set[tuple[int, int]]) -> tuple[int, int]:
    """
    Solves a system of modular equations using the Chinese Remainder Theorem.

    Yields:
        int: The solution to the given equations.
        int: The solution to the extended system with an additional equation (-7 mod 11).
    """
    r, m = chinese_remainder(equations, get_modulo=True)
    return r, chinese_remainder({(r, m), (-7, 11)})[0]
