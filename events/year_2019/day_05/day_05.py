"""
Advent of Code - Year 2019 - Day 5
https://adventofcode.com/2019/day/5
"""

from events.year_2019.ship_computer import Program


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a comma-separated string of integers into a list of integers.
    """
    return list(map(int, puzzle_input.split(',')))


def solver(integers: list[int]):
    """
    Executes the Program with the provided integers, yielding the first non-zero output from input
    1 and the output from input 5.
    """
    test_program = Program(integers)
    while True:
        output = test_program.run(1)
        if (output is None) or (output != 0):
            break
    yield output
    yield Program(integers).run(5)
