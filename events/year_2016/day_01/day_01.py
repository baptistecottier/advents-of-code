"""Advent of Code - Year 2016 - Day 01"""

from dataclasses import dataclass
from pythonfw.classes import Point


@dataclass
class Instruction:
    """A class representing a movement instruction in a grid system.

    The Instruction class holds information about movement in a 2D grid,
    including direction and distance.

    Attributes:
        dx (int): The change in x-coordinate (horizontal movement)
        dy (int): The change in y-coordinate (vertical movement) 
        n_blocks (int): Number of blocks to move in the specified direction
    """
    dx: int
    dy: int
    n_blocks: int


def preprocessing(puzzle_input: str) -> list[Instruction]:
    """
    Processes a string of directions into a list of Instructions.

    The function takes a string of comma-separated directions and converts them into a list
    of Instructions for navigation. Each direction consists of a turn ('L' for left, 'R' for right)
    followed by a number of steps.

    The function maintains a direction state using 'face' which rotates through four cardinal
    directions: North (0), West (1), South (2), and East (3).

    Parameters:
        data (str): A string of comma-separated directions (e.g., "L4, R3, L2")

    Returns:
        list[Instruction]: A list of Instruction objects, each containing:
            - x-coordinate movement (-1, 0, or 1)
            - y-coordinate movement (-1, 0, or 1)
            - number of steps to take in that direction

    Example:
        >>> preprocessing("L4, R3")
        [Instruction(0, -1, 4), Instruction(1, 0, 3)]
    """
    ways = [(1,0) , (0, -1), (-1, 0), (0,1)]
    face  = 0
    path = []
    for step in puzzle_input.split(', '):
        match step[0]:
            case 'L': face = (face - 1) % 4
            case 'R': face = (face + 1) % 4
        path.append(Instruction(*ways[face], int(step[1:])))
    return path


def solver(path: list[Instruction]):
    """
    Solves the navigation puzzle by processing a list of movement instructions.

    Args:
        path (list[Instruction]): A list of Instruction objects, each specifying a direction and the
            number of blocks to move.

    Returns:
        tuple[int, Optional[int]]: A tuple containing:
            - The Manhattan distance from the starting point to the final position after processing all
              instructions.
            - The Manhattan distance to the first location visited twice, or None if no location is
              visited twice.
    """
    pos     = Point()
    visited = {pos.xy()}
    twice   = None

    while path:
        instr = path.pop(0)
        for _ in range(instr.n_blocks):
            pos.move(instr.dx, instr.dy)
            if twice is None and pos.xy() in visited:
                twice = pos.manhattan()
            visited.add(pos.xy())
    return (pos.manhattan(), twice)
