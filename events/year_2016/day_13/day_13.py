"""Advent of Code - Year 2016 - Day 13"""

from itertools import product
from pythonfw.functions import bfs

def preprocessing(puzzle_input: str) -> set[tuple[int, int]]:
    """
    Creates a maze based on a given input number using binary calculations.
    
    Args:
        puzzle_input (str): The input number as a string
    Returns:
        set: Coordinates (x,y) representing open spaces in the maze
    """
    n = int(puzzle_input)
    maze = set()
    for x, y in product(range(50), repeat = 2):
        v = x * (x + 3 + 2 * y) + y * (1 + y) + n
        if bin(v).count('1') % 2 == 0:
            maze.add((x, y))
    return maze


def solver(maze: set[tuple[int, int]], x_end: int = 31, y_end: int = 39):
    """
    Solves two maze problems: shortest path to (x_end, y_end) and number of locations reachable
    within 50 steps from (1, 1).

    Args:
        maze (set[tuple[int, int]]): Set of wall coordinates in the maze.
        x_end (int, optional): Target x-coordinate. Defaults to 31.
        y_end (int, optional): Target y-coordinate. Defaults to 39.

    Yields:
        int: Shortest path length to (x_end, y_end).
        int: Number of locations reachable within 50 steps from (1, 1).
    """
    yield bfs(maze, (1,1), (x_end, y_end))

    distances = [bfs(maze, (1, 1), (x, y), 50) for x in range(51) for y in range(51 - x)]
    yield sum(distance != -1 for distance in distances)
