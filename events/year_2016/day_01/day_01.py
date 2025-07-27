"""
Advent of Code - Year 2016 - Day 1
https://adventofcode.com/2016/day/1
"""

# Standard import
from dataclasses import dataclass

# First class import
from pythonfw.classes import Point


@dataclass
class Instruction:
    """
    A class representing a movement instruction in a grid system.

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
    Parses the puzzle input into a list of Instruction objects representing movement steps.

    Args:
        puzzle_input (str): A string of comma-separated movement instructions (e.g., "R2, L3").

    Returns:
        list[Instruction]: A list of Instruction objects with direction and step count.

    Example:
        >>> preprocessing("R2, L3")
        [Instruction(0, -1, 2), Instruction(-1, 0, 3)]
    """
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    face = 0
    path = []
    for step in puzzle_input.split(", "):
        match step[0]:
            case "L":
                face = (face - 1) % 4
            case "R":
                face = (face + 1) % 4
        path.append(Instruction(*directions[face], int(step[1:])))
    return path


def solver(path: list[Instruction]) -> tuple[int, int]:
    """
    Solves the navigation puzzle by following a list of instructions and tracking visited positions.

    Args:
        path (list[Instruction]): A list of movement instructions.

    Returns:
        tuple[int, int]: A tuple containing:
            - The Manhattan distance from the starting point to the final position.
            - The Manhattan distance to the first location visited twice (0 if none).

    Example:
        >>> solver([Instruction(0, -1, 2), Instruction(-1, 0, 3)])
        (5, 0)
    """
    pos = Point()
    visited = {pos.xy()}
    twice = 0

    while path:
        instr = path.pop(0)
        for _ in range(instr.n_blocks):
            pos.move(instr.dx, instr.dy)
            if twice == 0 and pos.xy() in visited:
                twice = pos.manhattan()
            visited.add(pos.xy())
    return pos.manhattan(), twice
