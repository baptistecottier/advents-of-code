"""
Advent of Code - Year 2019 - Day 21
https://adventofcode.com/2019/day/21
"""

# Standard imports
from collections.abc import Iterator

# First party imports
from events.year_2019.ship_computer import Program


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a comma-separated string of integers into a list of integers.
    """
    return list(map(int, puzzle_input.split(',')))


def solver(intcode: list[int]) -> Iterator[int]:
    """
    Yields the hull damage reported by the springdroid when walking (part 1), then when running
    with the extended sensors (part 2).
    """
    # not A or (not C and D)
    rules = "NOT A J\nNOT C T\nAND D T\nOR T J\nWALK\n"
    yield run_robot(intcode, rules)

    # not A or (not C and D and H) or (not B and D and H)
    rules = "NOT A J\nNOT C T\nAND D T\nAND H T\nOR T J\nNOT B T\nAND D T\nAND H T\nOR T J\nRUN\n"
    yield run_robot(intcode, rules)


def run_robot(intcode: list[int], rules: str) -> int:
    """
    Sends the springscript to the springdroid as ASCII and returns the hull damage it reports,
    the first output that is not an ASCII character.
    """
    program = Program(intcode)
    springscript = list(rules.encode())

    while (output := program.run(*springscript)) is not None:
        if output >= 256:
            return output
    raise ValueError("The springdroid fell into space")
