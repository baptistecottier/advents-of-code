"""
Advent of Code - Year 2017 - Day 11
https://adventofcode.com/2017/day/11
"""

from pythonfw.classes import Point


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Returns puzzle input as a list of values separated by a comma"""
    return puzzle_input.split(",")


def solver(directions: list[str]) -> tuple[int, int]:
    """
    Calculate the shortest path distance from origin to final position and the maximum distance
    reached during the path, given a list of hex grid directions.

    The function processes directions on a hex grid using cube coordinates where:
    - 'nw' moves northwest (x-1, y-1)
    - 'n' moves north (y-1)
    - 'ne' moves northeast (x+1, y unchanged)
    - 'se' moves southeast (x+1, y+1)
    - 's' moves south (y+1)
    - 'sw' moves southwest (x-1, y unchanged)

    Args:
        directions (list): List of string directions ('nw', 'n', 'ne', 'se', 's', 'sw')

    Returns:
        tuple: A pair containing:
            - The final distance from origin after following all directions
            - The maximum distance from origin reached at any point during the path
    """
    path = []
    pos = Point()

    for step in directions:
        match step:
            case "nw":
                pos.move(-1, -1)
            case "n":
                pos.move(0, -1)
            case "ne":
                pos.move(1, 0)
            case "se":
                pos.move(1, 1)
            case "s":
                pos.move(0, 1)
            case "sw":
                pos.move(-1, 0)
        distance = max(abs(pos.x), abs(pos.y), abs(pos.x - pos.y))
        path.append(distance)

    return (path[-1], max(path))
