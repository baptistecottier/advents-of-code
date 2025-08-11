"""
Advent of Code - Year 2018 - Day 25
https://adventofcode.com/2018/day/25
"""

# Standard imports
from collections.abc import Iterator

# First party imports
from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Preprocesses puzzle input by extracting chunks of 4 integers.
    """
    return extract_chunks(puzzle_input, 4)


def solver(spacetime: list[list[int]]) -> Iterator[int]:
    """
    Groups spacetime coordinates into constellations based on Manhattan distance and returns the
    total count.
    """
    constellations = []
    constellation = [spacetime.pop()]
    while spacetime:
        size = len(constellation)
        for pos in spacetime:
            if any(distance(cc, pos) <= 3 for cc in constellation):
                constellation.append(pos)
                spacetime.remove(pos)
                break
        if len(constellation) == size:
            constellations.append(constellation)
            constellation = [spacetime.pop()]

    yield len(constellations) + 1


def distance(a: list[int], b: list[int]) -> int:
    """
    Calculate the Manhattan distance between two points represented as lists of integers.
    """
    return sum(abs(x - y) for x, y in zip(a, b))
