"""Advent of Code - Year 2017 - Day 02"""

from itertools  import permutations
from re         import split


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Preprocesses a puzzle input string by converting it into a list of integer lists.

    Args:
        puzzle_input (str): A string containing numbers separated by whitespace,
                           with each line representing a separate list.

    Returns:
        list[list[int]]: A list where each inner list contains the integers from
                         one line of the input string.

    Example:
        >>> preprocessing("5 1 9 5\\n7 5 3\\n2 4 6 8")
        [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
    """
    lines = [[int(n) for n in split(r'\s', line)] for line in puzzle_input.splitlines()]
    return lines


def solver(spreadsheet: list[list[int]]):
    """
    Calculates two checksums for a spreadsheet: the difference between max and min in each row,
    and the sum of the quotients of the only divisible pair in each row.

    Yields:
        int: The checksum (sum of row max-min differences).
        int: The sum of divisible quotients per row.
    """
    checksum = 0
    checkdiv = 0

    for row in spreadsheet:
        checksum += max(row) - min(row)
        for a, b in permutations(row, 2):
            if a % b == 0:
                checkdiv += a // b
                break

    yield checksum
    yield checkdiv
