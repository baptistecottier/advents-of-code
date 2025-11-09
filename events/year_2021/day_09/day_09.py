"""
Advent of Code - Year 2021 - Day 9
https://adventofcode.com/2021/day/9
"""

from math import prod
from collections import defaultdict


def _default_border_value() -> int:
    """Default value used for positions outside the parsed heightmap (simulate border = 9)."""
    return 9


def preprocessing(puzzle_input: str) -> dict[tuple[int, int], int]:
    """
    Converts a multiline string of digits into a dictionary mapping (x, y) coordinates to integer
    values, defaulting to 9 to simulate borders.
    """
    cave = defaultdict(_default_border_value)
    for y, row in enumerate(puzzle_input.splitlines(), 1):
        for x, n in enumerate(row, 1):
            cave[(x, y)] = int(n)
    return cave


def solver(cave: dict[tuple[int, int], int]) -> tuple[int, int]:
    """
    Solves the cave heightmap puzzle by yielding the sum of risk levels of all low points and the
    product of the sizes of the three largest basins.
    """
    neighbours = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    low_points = {(x, y) for x, y in list(cave)
                  if all(cave[(x, y)] < cave[(x + dx, y + dy)]
                         for dx, dy in neighbours)}
    return (len(low_points) + sum(cave[pos] for pos in low_points),
            prod(sorted(basin_size(cave, pos, set()) for pos in low_points)[-3:]))


def basin_size(cave: dict[tuple[int, int], int], pos: tuple[int, int], visited: set[tuple[int, int]]
               ) -> int:
    """
    Recursively computes the size of a basin in the cave starting from the given position, avoiding
    positions with value 9 and already visited positions.
    """
    x, y = pos
    if cave[(x, y)] == 9 or (x, y) in visited:
        return 0
    visited.add(pos)
    return 1 + sum(basin_size(cave, (x + dx, y + dy), visited)
                   for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)))
