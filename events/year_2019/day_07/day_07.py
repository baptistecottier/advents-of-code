"""
Advent of Code - Year 2019 - Day 7
https://adventofcode.com/2019/day/7
"""

# Standard imports
from collections.abc import Iterator
from itertools import permutations

# First party import
from events.year_2019.ship_computer import Program


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a comma-separated string of integers into a list of integers.
    """
    return list(map(int, puzzle_input.split(',')))


def solver(intcode: list[int]) -> Iterator[int]:
    """
    Yields the highest output signal that can be sent to the thrusters for both amplifier
    configurations using the provided Intcode program.
    """
    highest = 0
    for setting in permutations([0, 1, 2, 3, 4]):
        signal = 0
        for phase in setting:
            program = Program(intcode, phase)
            signal = program.run(signal)
        highest = max(highest, signal)
    yield highest

    highest = 0
    for setting in permutations([5, 6, 7, 8, 9]):
        signal = 0
        programs = [Program(intcode, phase) for phase in setting]
        while all((not program.halt for program in programs)):
            for program in programs:
                signal = program.run(signal)
                if signal is not None:
                    highest = max(highest, signal)
    yield highest
