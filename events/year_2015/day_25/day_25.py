"""Advent of Code - Year 2015 - Day 25"""

from re import findall


def preprocessing(puzzle_input: str) -> tuple[int, int]:
    """
    Extract all integers from the puzzle input and return them as a tuple.
    """
    numbers = [int(n) for n in findall(r'[0-9]+', puzzle_input)]
    if len(numbers) != 2:
        raise ValueError("Puzzle input must contain two numbers")
    return numbers[0], numbers[1]


def solver(row: int, col: int):
    """
    Calculate a specific value using a mathematical formula based on row and column inputs.

    Args:
        row (int): The row number.
        col (int): The column number.

    Yields:
        int: The calculated value using the formula described in the puzzle.
    """
    e = (row + col) * (row + col - 1) // 2 - row
    yield 20151125 * pow(252533, e, 33554393) % 33554393
