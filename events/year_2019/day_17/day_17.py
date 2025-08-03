"""
Advent of Code - Year 2019 - Day 17
https://adventofcode.com/2019/day/17
"""

from pythonfw.classes import Particule2D
from events.year_2019.ship_computer import Program


def preprocessing(puzzle_input: str) -> tuple[int, ...]:
    """
    Converts a comma-separated string of integers into a tuple of integers.
    """
    return tuple(map(int, puzzle_input.split(',')))


def solver(*intcode: int):
    """
    Processes an Intcode program output to identify scaffold intersections and yields the sum of
    their alignment parameters.
    """
    program = Program(intcode)
    scaffold = set()
    x, y = 0, 0

    while (output := program.run()) >= 0:
        match output:
            case 10:
                x, y = -1, y + 1
            case 35:
                scaffold.add((x, y))
            case 46:
                pass
            case _:
                Particule2D(
                    (x, y),
                    {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}[chr(output)])
        x += 1

    intersections = {
        (x, y)
        for x, y in scaffold
        if all(
            neighbor in scaffold
            for neighbor in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        )
    }
    yield sum(x * y for x, y in intersections)
