"""
Advent of Code - Year 2021 - Day 25
https://adventofcode.com/2021/day/25
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> tuple[set, set, int, int]:
    """
    Parses the puzzle input and returns the positions of '>' and 'v' characters as sets, along with
    the grid's width and height.
    """
    west = set()
    south = set()
    x = -1
    y = -1
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(row):
            match c:
                case '>': west.add((x, y))
                case 'v': south.add((x, y))
    return west, south, x + 1, y + 1


def solver(west: set[tuple[int, int]], south: set[tuple[int, int]], w: int, h: int
           ) -> Iterator[int]:
    """
    Simulates the movement of west- and south-facing entities on a toroidal grid until no movement
    occurs, yielding the number of steps taken.
    """
    steps = 0
    while steps := steps + 1:
        old_west = west
        old_south = south

        occupied = west.union(south)
        west = {((x + 1) % w, y) if ((x + 1) % w, y) not in occupied else (x, y)
                for (x, y) in west}

        occupied = west.union(south)
        south = {(x, (y + 1) % h) if (x, (y + 1) % h) not in occupied else (x, y)
                 for (x, y) in south}

        if old_west == west and old_south == south:
            break

    yield steps
