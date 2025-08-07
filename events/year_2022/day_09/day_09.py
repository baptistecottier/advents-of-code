"""
Advent of Code - Year 2022 - Day 9
https://adventofcode.com/2022/day/9
"""

from collections.abc import Iterator
from pythonfw.functions import sign


def preprocessing(puzzle_input: str) -> list[tuple[int, int]]:
    """
    Converts a puzzle input string of movement instructions into a list of (x, y) coordinates
    representing the path taken.
    """
    x, y = 0, 0
    path = [(x, y)]
    orientation = {'D': (0, -1), 'L': (-1, 0),  'R': (1, 0), 'U': (0, 1)}

    for direction, step in [ins.split(' ') for ins in puzzle_input.splitlines()]:
        step = int(step)
        (dx, dy) = orientation[direction]
        path.extend((x + i * dx, y + i * dy) for i in range(1, step + 1))
        (x, y) = (x + step * dx, y + step * dy)

    return path


def solver(path: list[tuple[int, int]]) -> Iterator[int]:
    """
    Yields the number of unique positions visited by the tail knot at the first and last iterations
    while traversing a given path.
    """
    for knot in range(9):
        tx, ty = 0, 0
        visited = []
        for (hx, hy) in path:
            if abs(hy - ty) > 1 or abs(hx - tx) > 1:
                tx += sign(hx - tx)
                ty += sign(hy - ty)
            visited.append((tx, ty))

        path = visited
        if knot in [0, 8]:
            yield len(set(visited))
