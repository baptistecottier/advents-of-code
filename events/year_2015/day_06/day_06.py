"""Advent of Code - Year 2015 - Day 06"""

from dataclasses import dataclass
from itertools import product


@dataclass
class Instruction:
    """A class representing a light instruction with coordinates.

    This class encapsulates an instruction for manipulating lights in a grid, containing
    an action to perform and the coordinates of the area affected.

    Attributes:
        action (int): The type of action to perform on the lights:
            0 for turn off
            1 for turn on
            2 for toggle
        sx (int): Starting x-coordinate of the affected area
        sy (int): Starting y-coordinate of the affected area 
        ex (int): Ending x-coordinate of the affected area
        ey (int): Ending y-coordinate of the affected area
    """
    action: int
    sx: int
    sy: int
    ex: int
    ey: int


def preprocessing(puzzle_input: str) -> list[Instruction]:
    """
    Process puzzle input into a list of lighting instructions.

    Args:
        puzzle_input (str): Raw puzzle input string containing lighting instructions

    Returns:
        list[Instruction]: List of Instruction objects containing operation and coordinates
    """
    instructions  = []
    for instruction in puzzle_input.splitlines():
        data = instruction.split(' ')
        start = list(map(int, data[-3].split(',')))
        end = list(map(int, data[-1].split(',')))
        match data[1]:
            case "off":
                op = 0
            case "on":
                op = 1
            case _:
                op = 2
        instructions.append(Instruction(op, *start, *end))
    return instructions


def solver(instructions: list[Instruction]):
    """
    Solve Day 6 puzzle by applying instructions to grid with different light behaviors.

    Args:
        instructions (list[Instruction]): List of light instructions to process

    Yields:
        int: Total brightness after applying toggle instructions (part 1)
        int: Total brightness after applying dimming instructions (part 2)
    """
    yield apply_instructions(instructions, 2, lambda x: 1 - x        , False)
    yield apply_instructions(instructions, 0, lambda x: max(0, x - 1), True)


def apply_instructions(instructions: list[Instruction], toggle: int, func: callable, cumul: bool):
    """
    Apply lighting instructions to a 1000x1000 grid and return total light value.

    Args:
        instructions (list[Instruction]): List of lighting instructions
        toggle (int): Value representing toggle action
        func (callable): Function to apply when toggling lights
        cumul (bool): If True, adds action value to current light value, else sets it

    Returns:
        int: Sum of all light values after applying instructions
    """
    lights = [[0 for _ in range(1000)] for _ in range(1000)]

    for instr in instructions:
        if instr.action == toggle:
            for x, y in product(range(instr.sx, instr.ex + 1),
                                range(instr.sy, instr.ey + 1)):
                lights[x][y] = func(lights[x][y])
        else:
            for x, y in product(range(instr.sx, instr.ex + 1),
                                range(instr.sy, instr.ey + 1)):
                if cumul:
                    lights[x][y] += instr.action
                else:
                    lights[x][y] = instr.action
    return sum(sum(line) for line in lights)
