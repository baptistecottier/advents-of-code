"""
Advent of Code - Year 2017 - Day 19
https://adventofcode.com/2017/day/19
"""

from pythonfw.classes import Point


def preprocessing(puzzle_input: str) -> tuple[dict, Point]:
    """
    Process the puzzle input to extract the path and starting point.

    Args:
        puzzle_input: A string representing the puzzle input.

    Returns:
        A tuple containing:
        - A dictionary mapping coordinates (x, y) to characters in the path.
        - The starting Point object at the top of the path.
    """
    path = {}
    start = Point()
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(row):
            if c != " ":
                if y == 0:
                    start = Point(x, y)
                path[(x, y)] = c
    return path, start


def solver(routing: dict, pos: Point) -> tuple[str, int]:
    """
    Navigate through a routing path, collecting letters and counting steps.

    Args:
        routing: Dictionary mapping (x, y) coordinates to path characters.
        pos: Point object with current position.

    Returns:
        Tuple of (collected letters, total steps).
    """
    dx, dy = 0, 1
    letters = ""
    steps = 1

    while 1:
        turn = False
        while (pos.x + dx, pos.y + dy) in routing:
            if routing[pos.xy()] not in " |-":
                letters += routing[pos.xy()]
            pos.move(dx, dy)
            steps += 1

        for nx, ny in ((dy, dx), (dy, -dx) if dx else (-dy, dx)):
            if (pos.x + nx, pos.y + ny) in routing:
                dx, dy = nx, ny
                pos.move(dx, dy)
                steps += 1
                turn = True
                break

        if not turn:
            if routing.get(pos.xy(), " ") not in " |-":
                letters += routing[pos.xy()]
            return letters, steps
    raise ValueError("No path found!")
