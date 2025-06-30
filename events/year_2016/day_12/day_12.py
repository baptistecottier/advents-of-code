"""Advent of Code - Year 2016 - Day 12"""


def preprocessing(puzzle_input: str) -> list[list[str]]:
    """
    Splits input string into list of lists of strings, each sublist containing instruction
    components.

    Args:
        puzzle_input (str): Multiline string containing assembunny instructions

    Returns:
        list[list[str]]: List of lists, each sublist contains tokens of one instruction
    """
    return [line.split() for line in puzzle_input.splitlines()]


def solver(program: list[list[str]]):
    """
    Solves a specific puzzle by processing a given program and generating results based on extracted
    parameters.

    Args:
        program (list[list[str]]): A list of instructions, where each instruction is a list of 
        strings.
            The function expects specific values at certain indices:
                - program[2][1]: Used as the 'fibo' parameter (int).
                - program[16][1]: Used as the 'fa' parameter (int).
                - program[17][1]: Used as the 'fb' parameter (int).

    Yields:
        int: The computed result after performing a modified Fibonacci sequence calculation and
            applying additional arithmetic using 'fa' and 'fb'.

    Note:
        The function assumes the input 'program' has at least 18 instructions, each with at least 
        two elements, and that the relevant elements can be converted to integers.
    """
    fibo = int(program[2][1])
    fa   = int(program[16][1])
    fb   = int(program[17][1])
    a, b = 1, 1

    for f in range(fibo + 8):
        a, b = b, a + b
        if f == fibo:
            yield a + fa * fb
    yield a + fa * fb
