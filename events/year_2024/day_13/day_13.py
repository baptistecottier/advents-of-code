"""
Advent of Code - Year 2024 - Day 13
https://adventofcode.com/2024/day/13
"""

# Standard imports
from collections.abc import Iterator

# First party imports
from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Preprocessing extracts chunks of 6 integers from puzzle_input.
    Each chunk then corresponds to a machine.
    """
    return extract_chunks(puzzle_input, 6)


def solver(machines: list[list[int]]) -> Iterator[int]:
    """
    To solve, use the minimize_cost function. First without delta, then with a
    delta of 10_000_000_000_000.
    """
    for delta in [0, 10_000_000_000_000]:
        yield minimize_cost(machines, delta)


def minimize_cost(machines: list[list[int]], delta: int) -> int:
    """
    Each machine is a system of two equations and two unknowns. We then solve the systems,
    and if both unknowns are integers, the prize is reachable, and the tokens required
    are added to the total token cost.
    """
    tokens = 0
    for xa, ya, xb, yb, xt, yt in machines:
        u = (yb * (xt + delta) - xb * (yt + delta))/(xa * yb - xb * ya)
        if u.is_integer():
            v = ((xt + delta) - xa * u) / xb
            if v.is_integer():
                tokens += 3 * u + v
    return int(tokens)
