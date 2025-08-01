"""
Advent of Code - Year 2017 - Day 20
https://adventofcode.com/2017/day/20
"""

from pythonfw.classes import Particule
from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input: str) -> list[Particule]:
    """
    Convert puzzle input to a list of Particule objects.
    """
    return [Particule(*particule) for particule in extract_chunks(puzzle_input, 9)]


def solver(particules: list[Particule]) -> tuple[int, int]:
    """
    Solves two particle physics problems.

    Args:
        particules: A list of Particule objects with position, velocity, and acceleration.

    Yields:
        int: First, the index of the particule that will stay closest to the origin.
              Then, the number of particles left after collisions after 50 time steps.
    """
    closer_index = particules.index(min(particules))

    for _ in range(51):
        for particule in particules:
            particule.v.move(*particule.a.xyz())
            particule.p.move(*particule.v.xyz())
        positions = list(particule.p.xyz() for particule in particules)
        positions = set(item for item in positions if positions.count(item) > 1)
        particules = list(item for item in particules if item.p.xyz() not in positions)
    return closer_index, len(particules)
