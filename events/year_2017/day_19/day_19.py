"""Advent of Code - Year 2017 - Day 19"""

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
            if c != ' ':
                if y == 0:
                    start = Point(x, y)
                path[(x, y)] = c
    return path, start


def solver(routing, pos):
    """
    Navigate through a routing path and collect letters encountered.
    
    Traverses a path defined by coordinates in 'routing', starting at 'pos', following
    straight paths and turning at corners according to specific rules. Letters
    encountered along the way are collected. The function yields the collected letters
    and the total steps taken once the path ends.
    
    Args:
        routing (dict): A dictionary mapping (x, y) tuples to characters representing
                       the path layout.
        pos (object): An object with x, y attributes and move(dx, dy) and xy() methods
                     representing the current position on the path.
    
    Yields:
        str: The string of letters collected along the path.
        int: The total number of steps taken to complete the path.
    
    Note:
        The path is considered ended when no valid turn can be made.
    """
    dx, dy  = 0, 1
    letters = ""
    steps   = 1

    while 1:
        turn = False
        while (pos.x + dx, pos.y + dy) in routing:
            if routing[pos.xy()] not in ' |-':
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
            if routing.get(pos.xy(), ' ') not in ' |-':
                letters += routing[pos.xy()]
            yield letters
            yield steps
            break
