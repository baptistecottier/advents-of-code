"""
Advent of Code - Year 2017 - Day 14
https://adventofcode.com/2017/day/14
"""

# Stadard import
from collections.abc import Iterator

# First-party import
from events.year_2017.day_10 import day_10


def solver(salt: str) -> Iterator[int]:
    """
    Solves a maze puzzle based on knot hash.

    Args:
        salt (str): Base string used to generate the knot hash.

    Yields:
        int: First, the total number of cells in the maze.
        int: Second, the number of connected regions in the maze.
    """
    maze = set()
    for row in range(128):
        hex_hash = int(day_10.knot_hash(f"{salt}-{row}", 256), 16)
        maze.update(set((row, i) for i in range(128) if hex_hash >> i & 1))
    yield len(maze)

    n_regions = 0
    while maze:
        region = [maze.pop()]
        while region:
            (x, y) = region.pop()
            for candidate in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if candidate in maze:
                    region.append(candidate)
                    maze.remove(candidate)
        n_regions += 1
    yield n_regions
