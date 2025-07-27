"""
Advent of Code - Year 2015 - Day 25
https://adventofcode.com/2015/day/25
"""

from collections.abc import Iterator
from re import findall


def preprocessing(puzzle_input: str) -> tuple[int, int]:
    """
    Extracts two integers from the puzzle input string.

    Args:
        puzzle_input (str): Input string containing two numbers.

    Returns:
        tuple[int, int]: A tuple containing the two extracted integers.

    Raises:
        ValueError: If the input does not contain exactly two numbers.

    Example:
        >>> preprocessing("To continue, please consult the code grid in row 4, column 5.")
        (4, 5)
    """
    numbers = [int(n) for n in findall(r"[0-9]+", puzzle_input)]
    if len(numbers) != 2:
        raise ValueError("Puzzle input must contain two numbers")
    return numbers[0], numbers[1]


def solver(row: int, col: int) -> Iterator[int]:
    """
    Generates the code value at a given position in a grid using a specific formula.

    Args:
        row (int): The row index (1-based).
        col (int): The column index (1-based).

    Yields:
        int: The code value at the specified (row, col) position.

    Example:
        >>> next(solver(4, 2))
        32451966
    """
    e = (row + col) * (row + col - 1) // 2 - row
    yield 20151125 * pow(252533, e, 33554393) % 33554393
