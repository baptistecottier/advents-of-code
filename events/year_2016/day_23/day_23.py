"""
Advent of Code - Year 2016 - Day 23
https://adventofcode.com/2016/day/23
"""

from math import factorial


def preprocessing(puzzle_input: str) -> list[list[str]]:
    """
    Process the puzzle input string into a list of instruction lists.

    Each instruction in the input is split into two parts: the operation and its parameters.
    The split is performed at the first space character.

    Args:
        puzzle_input (str): Raw puzzle input string containing instructions, one per line

    Returns:
        list[list[str]]: A list where each element is a list containing:
            - first element: operation name
            - second element: operation parameters
    """
    return list(line.split(" ", 1) for line in puzzle_input.splitlines())


def solver(instructions: list[list[str]]) -> tuple[int, int]:
    """
    Solves the assembly code optimization problem by calculating factorial values with delta offset.

    Args:
        instructions (list[list[str]]): List of assembly instructions where each instruction is a
            list of strings.

    Returns:
        tuple[int, int]: Solutions for part 1 (factorial(7) + delta) and part 2
            (factorial(12) + delta).

    Example:
        >>> instructions = [['cpy', '1', 'a'], ..., ['cpy', '81', 'c'], ['cpy', '94', 'd']]
        >>> solver(instructions)
        (12345, 479001694)
    """
    delta = int(instructions[19][1][:-2]) * int(instructions[20][1][:-2])
    return factorial(7) + delta, factorial(12) + delta
