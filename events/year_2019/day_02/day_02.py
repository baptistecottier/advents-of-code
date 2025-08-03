"""
Advent of Code - Year 2019 - Day 2
https://adventofcode.com/2019/day/2
"""

from events.year_2019.ship_computer import Program


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts comma-separated string of integers into a list of integers.
    """
    return list(map(int, puzzle_input.split(',')))


def solver(integers: list[int]):
    """
    Solves a puzzle by running a Program with given integers and yields two computed results based
    on memory manipulations.
    """
    program: Program = Program(integers)
    program.run()
    delta = program.memory[0]

    program = Program([integers[0], 1, *integers[2:]])
    program.run()
    modulo = program.memory[0] - delta

    yield delta + 12 * modulo + 2

    target = 19_690_720 - delta
    yield target // modulo * 100 + (target % modulo)
