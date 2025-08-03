"""
Advent of Code - Year 2019 - Day 19
https://adventofcode.com/2019/day/19
"""

# Standard imports
from itertools import product

# First party import
from events.year_2019.ship_computer import Program


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a comma-separated string of integers into a list of integers.
    """
    return list(map(int, puzzle_input.split(',')))


def solver(intcode: list[int]) -> tuple[int, int]:
    """
    Calculates the number of points affected by a beam in a 50x50 grid and finds the coordinates
    for fitting a 100x100 square within the beam, returning both results as a tuple.
    """
    beam = x = y = 0

    for tx, ty in product(range(50), repeat=2):
        if Program(intcode).run(tx, ty):
            beam += 1
            x, y = tx, ty

    while not Program(intcode).run(x - 99, y + 99):
        while Program(intcode).run(x, y):
            x += 1
        y += 1

    return beam, 10_000 * (x - 100) + y - 1
