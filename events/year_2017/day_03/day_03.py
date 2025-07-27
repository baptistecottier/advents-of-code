"""
Advent of Code - Year 2017 - Day 3
https://adventofcode.com/2017/day/3
"""

from collections import defaultdict
from collections.abc import Iterator
from itertools import product


def preprocessing(puzzle_input: str) -> int:
    """
    Converts puzzle input into an integer"""
    return int(puzzle_input)


def solver(square_position: int) -> Iterator[int]:
    """
    Solves a spiral grid problem for a given square position.

    Args:
        square_position: Position of the square in the spiral grid.

    Yields:
        First, the Manhattan distance from the square to the center.
        Second, the first value in the spiral memory that exceeds the square position.
    """
    circle_index = int(((square_position - 1) ** 0.5 + 1) // 2)
    if circle_index != 0:
        yield circle_index + (square_position - 1) % circle_index
    else:
        yield circle_index + (square_position - 1)

    x, y = 0, 0
    memory = defaultdict(int)
    dx, dy = (0, -1)
    value = 1
    turn = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}

    while value < square_position:
        tx, ty = turn[(dx, dy)]
        memory[(x, y)] = value
        if not memory[(x + tx, y + ty)]:
            dx, dy = tx, ty
        x, y = x + dx, y + dy
        value = sum(
            memory[(x + tx, y + ty)] for (tx, ty) in product({-1, 0, 1}, repeat=2)
        )
    yield value
