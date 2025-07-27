"""
Advent of Code - Year 2016 - Day 12
https://adventofcode.com/2016/day/12
"""

from collections.abc import Iterator


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


def solver(program: list[list[str]]) -> Iterator[int]:
    """
    Computes Fibonacci sequence values and yields results at specific positions.


    Args:
        program: List of instruction lists containing numeric values at specific indices.

    Yields:
        int: Fibonacci value plus product of two factors at position fibo, and final result after
             fibo+8 iterations.
    """
    fibo = int(program[2][1])
    fa = int(program[16][1])
    fb = int(program[17][1])
    a, b = 1, 1

    for f in range(fibo + 8):
        a, b = b, a + b
        if f == fibo:
            yield a + fa * fb
    yield a + fa * fb
