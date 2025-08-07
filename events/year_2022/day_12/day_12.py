"""
Advent of Code - Year 2022 - Day 12
https://adventofcode.com/2022/day/12
"""

# Standard imports
from collections import defaultdict

# First party imports
from pythonfw.functions import bfs


def preprocessing(puzzle_input: str
                  ) -> tuple[dict[tuple[int, int], int], list[tuple[int, int]], tuple[int, int]]:
    """
    Parses the puzzle input into a grid of elevations, a list of starting points, and the end point
    coordinates.
    """
    grid = defaultdict(int)
    starting_points = []
    end = (-1, -1)

    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            match c:
                case 'a':
                    grid[(x, y)] = 1
                    starting_points.append((x, y))
                case 'S':
                    grid[(x, y)] = 0
                    starting_points.insert(0, (x, y))
                case 'E':
                    grid[(x, y)] = 27
                    end = (x, y)
                case _: grid[(x, y)] = ord(c) - ord('a') + 1

    if end == (-1, -1):
        raise ValueError("No end point found!")
    return grid, starting_points, end


def solver(
        heightmap: dict[tuple[int, int], int],
        starting_points: list[tuple[int, int]],
        end: tuple[int, int]):
    """
    Solves the maze by computing the shortest distances from multiple starting points to the end
    point using BFS and returns the first and minimum positive distance.
    """
    distances = []
    for start in starting_points:
        distances.append(bfs(heightmap, start, end, predicate_arg=climbable))

    return distances[0], min(dist for dist in distances if dist > 0)


def climbable(pos: tuple[int, int], new: tuple[int, int], heightmap: dict[tuple[int, int], int]):
    """
    Determines if moving from the current position to a new position is allowed based on the height
    difference in the heightmap.
    """
    return new in heightmap and (heightmap[new] - heightmap[pos]) < 2
