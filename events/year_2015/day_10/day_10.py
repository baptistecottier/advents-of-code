"""
Advent of Code - Year 2015 - Day 10
https://adventofcode.com/2015/day/10
"""

from itertools import groupby


def solver(digits: str, iterations: int = 40) -> tuple[int, int]:
    """
    Solves both parts of the puzzle by applying Conway's Look-and-Say sequence.

    Args:
        digits (str): Initial sequence of digits
        iterations (int, optional): Number of iterations for part 1. Defaults to 40.

    Returns:
        tuple[int, int]: Length of resulting sequences for part 1 and part 2

    Examples:
        >>> solver("1", 1)
        (2, 6)  # Part 1: "1" -> "11" (length 2), Part 2: after 11 iterations (length 6)
        >>> solver("11", 1)
        (2, 6)  # Part 1: "11" -> "21" (length 2), Part 2: after 11 iterations (length 6)
    """
    return conway(digits, iterations), conway(digits, iterations + 10)


def conway(digits: str, iterations: int) -> int:
    """
    Applies Conway's look-and-say sequence for a given number of iterations.

    The look-and-say sequence is generated by reading off the digits of the previous value,
    counting the number of consecutive digits that are the same, and concatenating them together.
    For example: 1 is read off as "one 1" or 11, 11 is read off as "two 1s" or 21.

    Args:
        digits (str): The initial sequence of digits to apply the look-and-say operation on.
        iterations (int): The number of times to apply the look-and-say operation.

    Returns:
        int: The length of the resulting sequence after the specified number of iterations.

    Example:
        >>> conway("1", 1)
        2  # "1" becomes "11" (length 2)
        >>> conway("1", 2)
        2  # "1" -> "11" -> "21" (length 2)
    """
    for _ in range(iterations):
        digits = "".join(f"{len(list(l))}{k}" for k, l in groupby(digits))
    return len(digits)
