"""
Advent of Code - Year 2024 - Day 8
https://adventofcode.com/2024/day/8
"""

from collections import defaultdict
from itertools import combinations
from math import gcd


def preprocessing(puzzle_input: str) -> tuple[list[list[tuple[int, int]]], int, int]:
    """
    Browse puzzle input and retrieve positions of the antennas. As we won't need antennas name to
    solve the puzzles, only the positions grouped by antenna are returned.
    """
    x = y = -1
    antennas = defaultdict(list)

    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c != '.':
                antennas[c].append((x, y))

    return list(antennas.values()), x + 1, y + 1


def solver(antennas: list[list[tuple[int, int]]], width: int, height: int) -> tuple[int, int]:
    """
    For each antenna and for each pair of locations by antenna, we register all positions in line
    with these pair of locations. In order to solve part one, we diffentiate locations directly
    next to the antenna from the other ones.
    """
    locations = {0: set(), 1: set()}
    for antenna in antennas:
        for ((xa, ya), (xb, yb)) in combinations(antenna, 2):
            (dx, dy) = (xb - xa, yb - ya)
            k = gcd(dx, dy)
            (dx, dy) = (dx // k, dy // k)
            for delta in range(max(xa, ya)):
                for x, y in ((xa - delta * dx, ya - delta * dy),
                             (xb + delta * dx, yb + delta * dy)):
                    if (0 <= x < width) and (0 <= y < height):
                        locations[delta == 1].add((x, y))

    return len(locations[1]), len(locations[0].union(locations[1]))
