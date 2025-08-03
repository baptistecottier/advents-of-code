"""
Advent of Code - Year 2019 - Day 15
https://adventofcode.com/2019/day/15
"""

# Standard imports
from collections import deque

# First party imports
from events.year_2019.ship_computer import Program
from pythonfw.functions import bfs


def preprocessing(puzzle_input: str) -> tuple[int, ...]:
    """
    Converts a comma-separated string of integers into a tuple of integers.
    """
    return tuple(map(int, puzzle_input.split(',')))


def solver(*intcode: int) -> tuple[int, int]:
    """
    Solves the maze using an Intcode program, returning the shortest path to the oxygen system and
    the time to fill the area with oxygen.
    """
    maze, (pos, distance) = intcode_bfs(intcode)
    return distance, max(bfs(maze, pos, pt) for pt in maze)


def intcode_bfs(intcode: tuple[int, ...]) -> tuple[
        set[tuple[int, int]],
        tuple[tuple[int, int], int]]:
    """
    Performs a breadth-first search (BFS) on an Intcode-based maze, returning the set of visited
    positions and the location and distance to the oxygen system.
    """
    x, y = 0, 0
    prog = Program(intcode)

    queue = deque([[(0, 0, intcode)]])
    maze = set([(0, 0)])
    oxygen = ((0, 0), 0)

    while queue:
        path = queue.popleft()
        x, y, intcode = path[-1]
        prog = Program(intcode)
        for move, (x2, y2) in enumerate(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)), 1):
            temp = Program(prog.get_memory())
            if (x2, y2) not in maze:
                if (n := temp.run(move)):
                    if n == 2:
                        oxygen = ((x2, y2), len(path))
                    queue.append(path + [(x2, y2, temp.get_memory())])
                    maze.add((x2, y2))
    return maze, oxygen
