"""
Advent of Code - Year 2018 - Day 17
https://adventofcode.com/2018/day/17
"""

# Standard imports
from collections import deque
from collections.abc import Iterator
import re

# First-party imports
from pythonfw import functions as aocf


def preprocessing(puzzle_input: str) -> set[tuple[int, int]]:
    """
    Parse puzzle input to extract clay vein coordinates and return as a set of (x, y) positions.
    """
    example = False
    if example:
        puzzle_input = aocf.upload_example()

    clay = set()
    for vein in puzzle_input.splitlines():
        axis, start, end = map(int, re.findall(r'\d+', vein))
        if vein.startswith('x'):
            for y in range(start, end + 1):
                clay.add((axis, y))
        else:
            for x in range(start, end + 1):
                clay.add((x, axis))
    return clay


def solver(clay: set[tuple[int, int]]) -> Iterator[int]:
    """
    Simulates water flow through clay formations to find all reachable water positions.
    """
    water = set()
    max_depth = max(y for (_, y) in clay)
    springs = deque([(500, 0)])
    while springs:
        (x, y) = springs.popleft()
        while True:
            while (x, y + 1) not in clay and y > max_depth:
                water.add((x, y + 1))
                y += 1
    yield 0
    yield 0


def draw(clay: set[tuple[int, int]]) -> None:
    """
    Prints a visual representation of clay positions using '#' for clay and '.' for empty space.
    """
    max_depth = max(y for (_, y) in clay)
    max_width = max(x for (x, _) in clay)
    min_width = min(x for (x, _) in clay)
    for y in range(max_depth + 1):
        line = ""
        for x in range(min_width, max_width + 1):
            if (x, y) in clay:
                line += '#'
            else:
                line += '.'
        print(line)
