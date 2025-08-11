"""
Advent of Code - Year 2022 - Day 14
https://adventofcode.com/2022/day/14
"""

from collections.abc import Iterator
from re import findall


def preprocessing(puzzle_input: str) -> set[tuple[int, int]]:
    """
    Parses the puzzle input to extract rock coordinates and adds a floor at the maximum depth.
    """
    max_depth = 0
    rocks = set()

    for path in puzzle_input.splitlines():
        numbers = list(map(int, findall(r'[0-9]+', path)))
        xa, ya = numbers.pop(0), numbers.pop(0)
        while numbers:
            xa, ya, xb, yb = numbers.pop(0), numbers.pop(0), xa, ya
            if xa == xb:
                for dy in range(min(ya, yb), max(ya, yb) + 1):
                    rocks.add((xa, dy))
            else:
                for dx in range(min(xa, xb), max(xa, xb) + 1):
                    rocks.add((dx, ya))

    max_depth = max(y for _, y in rocks) + 2
    for x in range(1000):
        rocks.add((x, max_depth))
    return rocks


def solver(rocks: set[tuple[int, int]]) -> Iterator[int]:
    """
    Simulates sand falling through a grid of rocks and yields the sand count at the end of the
    endless phase and at rest.
    """
    x, y, sand = 500, 0, 0
    endless = True
    max_depth = max(y for _, y in rocks)
    while (500, 0) not in rocks:
        if (x, y + 1) not in rocks:
            y += 1
        elif (x - 1, y + 1) not in rocks:
            (x, y) = (x - 1, y + 1)
        elif (x + 1, y + 1) not in rocks:
            (x, y) = (x + 1, y + 1)
        else:
            rocks.add((x, y))
            (x, y) = (500, 0)
            sand += 1
        if endless and y > max_depth - 2:
            yield sand
            endless = False
    yield sand
