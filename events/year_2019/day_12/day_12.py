"""
Advent of Code - Year 2019 - Day 12
https://adventofcode.com/2019/day/12
"""

from math import lcm
from pythonfw.classes import Particule
from pythonfw.functions import extract_chunks, sign


def preprocessing(puzzle_input: str) -> set[Particule]:
    """
    Converts the puzzle input string into a set of Particule objects representing moons.
    """
    moons = {Particule(*moon) for moon in extract_chunks(puzzle_input, 3)}
    return moons


def solver(moons: set[Particule], steps: int = 1_000) -> tuple[int, int]:
    """
    Simulates the motion of a set of moons under gravity and yields the total energy after a given
    number of steps and the cycle length for the system to repeat.
    """
    coord = ['x', 'y', 'z']
    visited = {c: {tuple((getattr(m.p, c), 0)) for m in moons} for c in coord}
    cycles = {}
    step = 0
    energy_after_1_000_steps = -1
    while len(cycles) < 3 or step <= steps:
        if step == steps:
            energy_after_1_000_steps = sum(m.p.manhattan() * m.v.manhattan() for m in moons)
            for c in cycles:
                coord.remove(c)

        for c in coord.copy():
            for m, g in zip(moons, gravity(moons, c)):
                setattr(m.v, c, getattr(m.v, c) + g)
                setattr(m.p, c, getattr(m.p, c) + getattr(m.v, c))

            values = tuple((getattr(m.p, c), getattr(m.v, c)) for m in moons)
            if values in visited[c] and c not in cycles:
                cycles[c] = step
                coord.remove(c)
            else:
                visited[c].add(values)

        step += 1
    return energy_after_1_000_steps, lcm(*cycles.values())


def gravity(moons: set[Particule], attr: str) -> tuple[int, ...]:
    """
    Calculates the net gravitational effect on each moon along a given attribute axis and returns
    the results as a tuple.
    """
    return tuple(sum(sign(getattr(a.p, attr) - getattr(b.p, attr)) for a in moons) for b in moons)
