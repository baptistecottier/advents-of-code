"""
Advent of Code - Year 2016 - Day 19
https://adventofcode.com/2016/day/19
"""

from collections.abc import Iterator
from math import log


def preprocessing(puzzle_input: str) -> int:
    """
    Converts input string to integer.

    Args:
        puzzle_input (str): The input string to convert

    Returns:
        int: The converted integer
    """
    return int(puzzle_input)


def solver(nb_players: int) -> Iterator[int]:
    """
    Solves the Josephus problem for 2 and 3 removals.

    Args:
        nb_players (int): Number of players in the circle

    Yields:
        int: Solution for 2-player removal game
        int: Solution for 3-player removal game
    """
    for step in [2, 3]:
        yield solve_josephus(nb_players, step)


def solve_josephus(nb_players: int, base: int) -> int:
    """
    Solve the generalized Josephus problem for a given number of players and base.

    Args:
        nb_players (int): The total number of players in the circle.
        base (int): The step count or base for elimination.

    Returns:
        int: The position of the winning player (0-indexed).
    """
    logn = int(log(nb_players, base))
    winner = nb_players % (base**logn)
    if base - 1 < nb_players / (base**logn) < base:
        winner += base ** ((base - 2) * logn) + winner
    return winner
