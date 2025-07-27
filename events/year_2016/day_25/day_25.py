"""
Advent of Code - Year 2016 - Day 25
https://adventofcode.com/2016/day/25
"""

# Standard imports
from collections.abc import Iterator

# First-party imports
from pythonfw.classes import Register


def preprocessing(puzzle_input: str) -> list[tuple[int, str, str | int]]:
    """
    Processes assembly-like instructions into a list of tuples.

    Args:
        puzzle_input (str): Raw input string containing assembly instructions

    Returns:
        list[tuple[int, str, str | int]]: List of processed instructions as tuples
    """
    instructions = []
    for instruction in puzzle_input.splitlines():
        data = instruction.split()
        match data[0]:
            case "cpy":
                instructions.append((0, data[2], data[1]))
            case "inc":
                instructions.append((1, data[1], 1))
            case "dec":
                instructions.append((1, data[1], -1))
            case "jnz":
                instructions.append((2, data[1], int(data[2])))
            case "out":
                instructions.append((3, data[1], None))
    return instructions


def run(instructions: list[tuple[int, str, str | int]], a: int) -> int:
    """
    Execute assembly-like instructions with register manipulation and alternating pattern
    detection.

    Args:
        instructions: List of tuples containing (task_id, register_name, value/register)
        a: Initial value for register 'a'

    Returns:
        int: The input value 'a' if alternating pattern detected >10 times, else 0

    Examples:
        >>> instructions = [(1, 'a', 5), (3, 'a', 0)]
        >>> run(instructions, 10)
        10
        >>> run(instructions, 0)
        0
    """
    counter = -1
    tictac = 0
    instruction = 0
    register = Register(a, 0, 0, 0)

    while True:
        task, reg, val = instructions[instruction]
        if isinstance(val, str):
            register[reg] = register.get(val)

        else:
            match task:
                case 1:
                    register[reg] += val
                case 2:
                    if register.get(reg) != 0:
                        instruction += val - 1
                case 3:
                    if tictac == register[reg]:
                        counter += 1
                        if counter > 10:
                            return a
                        tictac = 1 - tictac
                    else:
                        return 0
        instruction += 1


def solver(instructions: list[tuple[int, str, str | int]]) -> Iterator[int]:
    """
    Incrementally test values for register a until a valid signal output is found.

    Args:
        instructions (list[tuple[int, str, str | int]]): List of assembly instructions as tuples.

    Yields:
        int: First valid signal output found.
    """
    register_a = 0
    signal = 0
    while signal == 0:
        register_a += 1
        signal = run(instructions, register_a)
    yield signal
