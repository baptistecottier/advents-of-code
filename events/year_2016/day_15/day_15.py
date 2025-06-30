"""Advent of Code - Year 2016 - Day 15"""

from re       import findall
from pythonfw.functions import chinese_remainder

def preprocessing(puzzle_input: str) -> set[tuple[int, int]]:
    """
    Process the puzzle input to extract equations from the disc configurations.

    This function takes a string input containing disc information and converts it into
    a set of tuples representing timing equations. Each tuple contains:
    - A negative sum of the initial position and disc number (-(ta + d))
    - The total number of positions for that disc (tn)

    Parameters:
        puzzle_input (str): A string containing the disc configurations
                           Format expected: numbers representing disc positions and timings

    Returns:
        set[tuple[int, int]]: A set of tuples, each containing two integers:
                             (-initial_position - disc_number, total_positions)

    Example:
        >>> input_str = "Disc #1 has 5 positions; at time=0, it is at position 4."
        >>> preprocessing(input_str)
        {(-5, 5)}  # Where -5 = -(4 + 1) and 5 is the total positions
    """
    values    = list(int(item) for item in findall(r'[0-9]+', puzzle_input))
    equations = set()
    while values:
        ta, _, tn, d = values.pop(), values.pop(), values.pop(), values.pop()
        equations.add((-(ta + d), tn))
    return equations


def solver(equations: set[tuple[int, int]]):
    """
    Solves a system of modular equations using the Chinese Remainder Theorem.

    Yields:
        int: The solution to the given equations.
        int: The solution to the extended system with an additional equation (-7 mod 11).
    """
    r, m = chinese_remainder(equations, get_modulo = True)
    yield r
    yield chinese_remainder({(r, m), (-7, 11)})[0]
