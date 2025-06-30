"""Advent of Code - Year 2016 - Day 08"""

import re
from itertools import product
from pythonfw.functions import screen_reader

def preprocessing(puzzle_input: str) -> list[tuple[int, int, int]]:
    """
    Process puzzle input into a sequence of display operations.

    This function takes a string input containing instructions for manipulating a display
    and converts it into a sequence of tuples representing three types of operations:
    - rect: (0, width, height) - turns on pixels in a rectangle of given width and height
    - rotate row: (1, row_index, shift) - rotates specified row by given number of pixels
    - rotate column: (2, col_index, shift) - rotates specified column by given number of pixels

    Args:
        puzzle_input (str): Multi-line string containing display manipulation instructions
                           in the format: "rect AxB" or "rotate row/column y=A by B"

    Returns:
        list: List of tuples, each containing:
              - Operation type (int): 0 for rect, 1 for rotate row, 2 for rotate column
              - First parameter (int): width/row index/column index
              - Second parameter (int): height/shift amount

    Example:
        >>> preprocessing("rect 3x2\\nrotate column x=1 by 1")
        [(0, 3, 2), (2, 1, 1)]
    """
    sequence = []
    for seq in puzzle_input.splitlines():
        data = re.split(r'[\sx=]', seq)
        match data[0], data[1]:
            case "rect", _:       sequence.append((0, int(data[1]),  int(data[2])))
            case "rotate", "row": sequence.append((1, int(data[-3]), int(data[-1])))
            case "rotate", _:     sequence.append((2, int(data[-3]), int(data[-1])))
    return sequence


def solver(sequence: list[tuple[int, int, int]], im: str = '50x6'):
    """
    Solves a screen manipulation puzzle by applying a sequence of operations to a virtual screen.

    Args:
        sequence (list[tuple[int, int, int]]): A list of operations, where each operation is a tuple
            (op, a, b). 'op' is the operation type (0: fill rectangle, 1: rotate row, 2: rotate 
            column), and 'a', 'b' are operation parameters.
        im (str, optional): The screen dimensions in the format 'widthxheight'. Defaults to '50x6'.

    Yields:
        int: The number of lit pixels on the screen after all operations.
        Any: The result of 'screen_reader(screen)' if the screen height is 6 or 10.
    """
    w, h = (int(item) for item in im.split('x'))
    screen = set()
    for op, a, b in sequence:
        match op:
            case 0:
                screen.update((x, y) for x, y in product(range(a), range(b)))
            case 1:
                screen = {(x if y != a else (x + b) % w, y) for (x, y) in screen}
            case 2:
                screen = {(x, y if x != a else (y + b) % h) for (x, y) in screen}
    yield len(screen)
    if h in [6, 10]:
        yield screen_reader(screen)
