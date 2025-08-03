"""
Advent of Code - Year 2019 - Day 3
https://adventofcode.com/2019/day/3
"""

from pythonfw.classes import Point


def preprocessing(puzzle_input: str) -> list[list[tuple[str, int]]]:
    """
    Parses the puzzle input into a list of lists, each containing (direction, distance) tuples for
    each wire segment.
    """
    paths = []
    for wire in puzzle_input.splitlines():
        wire_path = []
        for item in wire.split(','):
            wire_path.append((item[0], int(item[1:])))
        paths.append(wire_path)
    return paths


def solver(paths: list[list[tuple[str, int]]]) -> tuple[int, int]:
    """
    Finds the minimum Manhattan distance and minimum combined steps to an intersection between two
    wire paths.
    """
    directions = {'L': (-1, 0), 'U': (0, -1), 'R': (1, 0), 'D': (0, 1)}

    pos = Point()
    step = 0
    path = {pos.xy(): step}
    for turn, steps in paths.pop(0):
        dx, dy = directions[turn]
        for _ in range(steps):
            pos.move(dx, dy)
            path[pos.xy()] = (step := step + 1)

    pos = Point()
    step = 0
    distances = set()
    combined_steps = set()

    for turn, steps in paths.pop(0):
        dx, dy = directions[turn]
        for _ in range(steps):
            step += 1
            pos.move(dx, dy)
            if pos.xy() in path:
                distances.add(pos.manhattan())
                combined_steps.add(path[pos.xy()] + step)

    return min(distances), min(combined_steps)
