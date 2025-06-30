"""Advent of Code - Year 2016 - Day 23"""

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
    return list(line.split(' ', 1) for line in puzzle_input.splitlines())


def solver(instructions: list[list[str]]):
    """
    Solves the puzzle by computing two results based on parsed instructions.

    Args:
        instructions (list[list[str]]): The parsed instructions from the input.

    Yields:
        int: The computed result for two different cases.
    """
    delta = int(instructions[19][1][:-2]) * int(instructions[20][1][:-2])
    yield factorial(7) + delta
    yield factorial(12) + delta
