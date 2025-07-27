"""
Advent of Code - Year 2016 - Day 8
https://adventofcode.com/2016/day/8
"""

# Standard imports
from itertools import product
import re

# First-party import
from pythonfw.functions import screen_reader


def preprocessing(puzzle_input: str) -> list[tuple[int, int, int]]:
    """
    Parse puzzle input into a sequence of display operations.

    Args:
        puzzle_input: Raw puzzle input containing rect and rotate commands

    Returns:
        List of tuples where:
        - (0, width, height) for rect commands
        - (1, row, amount) for rotate row commands
        - (2, col, amount) for rotate column commands

    Examples:
        >>> preprocessing("rect 3x2\\nrotate row y=0 by 4\\nrotate column x=1 by 1")
        [(0, 3, 2), (1, 0, 4), (2, 1, 1)]
    """
    sequence = []
    for seq in puzzle_input.splitlines():
        data = re.split(r"[\sx=]", seq)
        match data[0], data[1]:
            case "rect", _:
                sequence.append((0, int(data[1]), int(data[2])))
            case "rotate", "row":
                sequence.append((1, int(data[-3]), int(data[-1])))
            case "rotate", _:
                sequence.append((2, int(data[-3]), int(data[-1])))
    return sequence


def solver(sequence: list[tuple[int, int, int]], im: str = "50x6") -> tuple[int, str]:
    """
    Solves a screen manipulation puzzle by applying a sequence of operations to a virtual screen.

    Args:
        sequence (list[tuple[int, int, int]]): A list of operations, where each operation is a tuple
            (op, a, b). 'op' is the operation type (0: fill rectangle, 1: rotate row, 2: rotate
            column), and 'a', 'b' are operation parameters.
        im (str, optional): The screen dimensions in the format 'widthxheight'. Defaults to '50x6'.

    Returns:
        tuple[int, str]: A tuple containing the number of lit pixels and the screen reader result.

    Examples:
        >>> sequence = [(0, 3, 2), (1, 0, 4), (2, 1, 1)]
        >>> count, result = solver(sequence, "7x3")
        >>> count
        6

        >>> sequence = [(0, 2, 1)]
        >>> count, result = solver(sequence, "5x6")
        >>> count
        2
    """
    w, h = (int(item) for item in im.split("x"))
    screen = set()
    for op, a, b in sequence:
        match op:
            case 0:
                screen.update((x, y) for x, y in product(range(a), range(b)))
            case 1:
                screen = {(x if y != a else (x + b) % w, y) for (x, y) in screen}
            case 2:
                screen = {(x, y if x != a else (y + b) % h) for (x, y) in screen}

    if h in [6, 10]:
        return len(screen), screen_reader(screen)

    raise ValueError("Screen height must be 6 or 10")
