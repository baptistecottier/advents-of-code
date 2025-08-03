"""
Advent of Code - Year 2019 - Day 10
https://adventofcode.com/2019/day/10
"""

# Standard import
from collections import defaultdict
from math import atan, degrees

# First party import
from pythonfw.functions import manhattan


def preprocessing(puzzle_input: str) -> set[tuple[int, int]]:
    """
    Parses the puzzle input and returns a set of (x, y) tuples representing asteroid positions.
    """
    belt = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, asteroid in enumerate(line):
            if asteroid == '#':
                belt.add((x, y))
    return belt


def solver(belt: set[tuple[int, int]]) -> tuple[int, int]:
    """
    Finds the asteroid with the best visibility and returns the number of visible asteroids from
    that location and a value based on the coordinates of the 200th asteroid to be vaporized.
    """
    asteroids = {}
    coord_ast = 0, 0
    for (x, y) in belt:
        angles = defaultdict(list)

        for (xx, yy) in belt:
            if (xx, yy) == (x, y):
                continue
            dx, dy = xx - x, yy - y
            div = (dx ** 2 + dy ** 2) ** (0.5)
            if dx + div != 0:
                angle = round(degrees(2 * atan(dy/(dx + div))), 5)
            else:
                angle = 180
            angles[(90 + angle) % 360].append((xx, yy))

        if len(angles.keys()) > len(asteroids.keys()):
            coord_ast, asteroids = (x, y), angles

    distances = {}
    for candidate in sorted(asteroids.items())[199][1]:
        distances[candidate] = manhattan(coord_ast, candidate)
    (x, y) = min(distances.keys(), key=lambda c: distances[c])

    return len(asteroids), 100 * x + y
