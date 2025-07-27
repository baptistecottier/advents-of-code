"""
Advent of Code - Year 2016 - Day 24
https://adventofcode.com/2016/day/24
"""

# Standard imports
from itertools import permutations, pairwise

# First-party imports
from pythonfw.functions import bfs


def preprocessing(puzzle_input: str) -> tuple[dict, int]:
    """
    Parse grid input and calculate shortest distances between numbered coordinates.

    Args:
        puzzle_input: Multi-line string representing a grid where '#' are walls,
                     '.' are open spaces, and digits are numbered coordinates.

    Returns:
        tuple: (distances dict mapping (src, dst) to shortest distance, number of coordinates)

    Example:
        >>> grid = "###7#\\n#1.2#\\n#####"
        >>> distances, n = preprocessing(grid)
        >>> distances[(1, 2)]  # distance between coordinates 1 and 2
        2
        >>> n  # number of coordinates found
        3
    """
    grid = set()
    coordinates = {}
    distances = {}

    for y, row in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(row):
            if c != "#":
                grid.add((x, y))
                if c.isdigit():
                    coordinates[int(c)] = (x, y)
    n_coord = len(coordinates)
    for src in range(n_coord):
        for dst in range(src + 1, n_coord):
            distance = bfs(grid, coordinates[src], coordinates[dst])
            distances[(src, dst)] = distance
            distances[(dst, src)] = distance
    return distances, n_coord


def solver(distances: dict, n_coord: int) -> tuple[int, int]:
    """
    Find shortest path visiting all coordinates and optionally returning to start.

    Args:
        distances: Dict mapping (src, dst) coordinate pairs to distances
        n_coord: Total number of coordinates (0 to n_coord-1)

    Returns:
        Tuple of (shortest_one_way_trip, shortest_round_trip)

    Examples:
        >>> distances = {(0,1): 2, (1,2): 3, (2,0): 4, (0,2): 5, (1,0): 2, (2,1): 3}
        >>> solver(distances, 3)
        (5, 9)
    """
    paths = set()
    for path in permutations(range(1, n_coord)):
        trip_length = distances[(0, path[0])]
        trip_length += sum(distances[(src, dst)] for src, dst in pairwise(list(path)))
        back_length = distances[(path[-1], 0)]
        paths.add((trip_length, back_length))

    return min(trip for trip, _ in paths), min(trip + back for trip, back in paths)
