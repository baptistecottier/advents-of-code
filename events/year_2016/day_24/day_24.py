"""Advent of Code - Year 2016 - Day 24"""

from itertools import permutations, pairwise
from pythonfw.functions import bfs


def preprocessing(puzzle_input: str) -> tuple[dict, int]:
    """
    Preprocesses the puzzle input to extract grid coordinates, numbered locations, and pairwise
    distances.

    Args:
        puzzle_input (str): The input string representing the puzzle grid, where '#' denotes walls
            and digits represent special coordinates.

    Returns:
        tuple[dict, int]: A tuple containing:
            - distances (dict): A dictionary mapping (src, dst) pairs of numbered locations to their
              shortest path distance, computed using BFS.
            - n_coord (int): The total number of numbered coordinates found in the grid.

    Notes:
        The function assumes that the BFS function is defined elsewhere and that all numbered 
        locations are single-digit integers.
    """
    grid        = set()
    coordinates = {}
    distances   = {}

    for y, row in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(row):
            if c != '#':
                grid.add((x, y))
                if c.isdigit():
                    coordinates[int(c)] = ((x, y))
    n_coord = len(coordinates)
    for src in range(n_coord):
        for dst in range(src + 1, n_coord):
            distance = bfs(grid, coordinates[src], coordinates[dst])
            distances[(src, dst)] = distance
            distances[(dst, src)] = distance
    return distances, n_coord


def solver(distances: dict, n_coord: int):
    """
    Calculate the shortest paths for a traveling salesman problem with optional return to start.

    This function finds the minimum distance for two scenarios:
    1. Visiting all points without returning to start
    2. Visiting all points and returning to start (round trip)

    Args:
        distances (dict): Dictionary of distances between pairs of coordinates
                         with format {(src, dst): distance}
        n_coord (int): Number of coordinates/points to visit

    Yields:
        int: Minimum distance without returning to start
        int: Minimum distance including return to start point

    Example:
        >>> distances = {(0,1): 2, (1,0): 2, (0,2): 3, (2,0): 3, (1,2): 4, (2,1): 4}
        >>> list(solver(distances, 3))
        [5, 7]
    """
    paths = set()
    for path in permutations(range(1, n_coord)):
        trip_length = distances[(0, path[0])]
        trip_length += sum(distances[(src, dst)] for src, dst in pairwise(list(path)))
        back_length = distances[(path[-1] , 0)]
        paths.add((trip_length, back_length))

    yield min(trip        for trip, _    in paths)
    yield min(trip + back for trip, back in paths)
