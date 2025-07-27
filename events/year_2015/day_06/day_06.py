"""
Advent of Code - Year 2015 - Day 6
https://adventofcode.com/2015/day/6
"""

from dataclasses import dataclass
from itertools import product


@dataclass
class Instruction:
    """
    Represents a light instruction with action type and coordinates for a rectangular region.
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

    Examples:
        >>> preprocessing("turn on 0,0 through 999,999")
        [Instruction(action=1, sx=0, sy=0, ex=999, ey=999)]

        >>> preprocessing("toggle 0,0 through 999,0")
        [Instruction(action=2, sx=0, sy=0, ex=999, ey=0)]

        >>> preprocessing("turn off 499,499 through 500,500")
        [Instruction(action=0, sx=499, sy=499, ex=500, ey=500)]
    """
    instructions = []
    for instruction in puzzle_input.splitlines():
        data = instruction.rsplit(" ", 3)
        start = list(map(int, data[1].split(",")))
        end = list(map(int, data[3].split(",")))
        match data[0]:
            case "turn off":
                op = 0
            case "turn on":
                op = 1
            case "toggle":
                op = 2
            case _:
                raise ValueError(f"Invalid instruction: {instruction}")
        instructions.append(Instruction(op, *start, *end))
    return instructions


def solver(instructions: list[Instruction]) -> tuple[int, int]:
    """
    Solves the light grid puzzle by applying instructions to two different light grids.

    Args:
        instructions: List of Instruction objects containing light operation details

    Returns:
        tuple: (sum of lights in unfixed_lights grid, sum of brightness in fixed_lights grid)

    Examples:
        >>> lights_on = solver([Instruction(action=1, sx=0, sy=0, ex=999, ey=999)])[0]
        >>> lights_on
        1000000

        >>> brightness = solver([Instruction(action=2, sx=0, sy=0, ex=999, ey=999)])[1]
        >>> brightness
        2000000

        >>> solver([Instruction(action=0, sx=499, sy=499, ex=500, ey=500)])
        (0, 0)
    """
    unfixed_lights = [[0 for _ in range(1000)] for _ in range(1000)]
    fixed_lights = [[0 for _ in range(1000)] for _ in range(1000)]

    for instr in instructions:
        for x, y in product(
            range(instr.sx, instr.ex + 1), range(instr.sy, instr.ey + 1)
        ):
            fixed_lights[x][y] = fix(instr.action, fixed_lights[x][y])

            if instr.action == 2:
                unfixed_lights[x][y] = 1 - unfixed_lights[x][y]
            else:
                unfixed_lights[x][y] = instr.action

    return (
        sum(sum(line) for line in unfixed_lights),
        sum(sum(line) for line in fixed_lights),
    )


def fix(action: int, light_state: int) -> int:
    """
    Updates the state of a light based on the given action.

    Args:
        action (int): The action to perform (0 to decrease, 1 or 2 to increase).
        light_state (int): The current state of the light.

    Returns:
        int: The updated state of the light.

    Examples:
        >>> fix(0, 3)
        2
        >>> fix(1, 2)
        3
        >>> fix(2, 0)
        2
    """
    if action == 0:
        light_state = max(0, light_state - 1)
    else:
        light_state += action

    return light_state
