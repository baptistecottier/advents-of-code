"""
Advent of Code - Year 2023 - Day 16
https://adventofcode.com/2023/day/16
"""

from collections import deque
from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Beam:
    """
    Represents a beam with position (x, y) and direction (dx, dy) on a grid.
    """
    x: int
    y: int
    dx: int
    dy: int


def preprocessing(puzzle_input: str) -> tuple[dict[tuple[int, int], str], int, int]:
    """
    Parses the puzzle input into a layout dictionary and returns it along with the width and height
    of the grid.
    """
    layout = {}
    x = y = -1

    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            layout[(x, y)] = c

    return layout, x + 1, y + 1


def solver(layout: dict[tuple[int, int], str], width: int, height: int) -> Iterator[int]:
    """
    Yields the energization value for the initial position and the maximum energization from all
    four edges of the layout.
    """
    yield energization(layout, width, height, Beam(0, 0, 1, 0))

    max_left = max(energization(layout, width, height, Beam(0, y, 1, 0))
                   for y in range(height))

    max_right = max(energization(layout, width, height, Beam(width - 1, y, -1, 0))
                    for y in range(height))

    max_top = max(energization(layout, width, height, Beam(x, 0, 0, 1))
                  for x in range(width))

    max_bottom = max(energization(layout, width, height, Beam(height - 1, x, 0, -1))
                     for x in range(width))

    yield max(max_left, max_right, max_top, max_bottom)


def energization(layout: dict[tuple[int, int], str], width: int, height: int, beam: Beam) -> int:
    """
    Simulates the movement of beams through a grid layout and returns the number of unique
    positions energized.
    """
    beams = deque([beam])
    energized = set()
    while beams:
        beam = beams.popleft()
        while 0 <= beam.x < width and 0 <= beam.y < height:
            if (beam.x, beam.y, beam.dx, beam.dy) in energized:
                break
            energized.add((beam.x, beam.y, beam.dx, beam.dy))

            match layout[(beam.x, beam.y)], beam.dx, beam.dy:
                case '/', _, _:
                    beam.dx, beam.dy = -beam.dy, -beam.dx

                case '\\', _, _:
                    beam.dx, beam.dy = beam.dy, beam.dx

                case '|', _, 0:
                    beam.dx = 0
                    beam.dy = 1
                    beams.append(Beam(beam.x, beam.y - 1, 0, -1))

                case '-', 0, _:
                    beam.dx = 1
                    beam.dy = 0
                    beams.append(Beam(beam.x - 1, beam.y, -1, 0))

            beam.x += beam.dx
            beam.y += beam.dy

    return len(set((x, y) for (x, y, _, _) in energized))
