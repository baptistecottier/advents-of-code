"""
Advent of Code - Year 2018 - Day 23
https://adventofcode.com/2018/day/23
"""

from collections.abc import Iterator
from re import findall
from z3 import If, Optimize, Ints, Sum


def preprocessing(puzzle_input: str) -> set[tuple[tuple[int, int, int], int]]:
    """
    Parse puzzle input to extract nanobot positions and signal radii.
    """
    nanobots = set()
    numbers = list(map(int, findall(r'-?[0-9]+', puzzle_input)))
    while numbers:
        nanobots.add(((numbers.pop(0), numbers.pop(0), numbers.pop(0)), numbers.pop(0)))
    return nanobots


def solver(nanobots: set[tuple[tuple[int, int, int], int]]) -> Iterator[int]:
    """
    Solves nanobot coordination problem by finding maximum reachable bots and optimal position
    closest to origin.
    """
    in_range = 0
    max_pos, max_r = max(nanobots, key=lambda n: n[1])
    for pos, _ in nanobots:
        if sum(abs(a - b) for a, b in zip(max_pos, pos)) <= max_r:
            in_range += 1
    yield in_range

    candidate = Ints("x y z")
    reachable = Sum(If(z3_dist(pos, candidate) <= r, 1, 0) for pos, r in nanobots)

    opt = Optimize()
    opt.maximize(reachable)
    opt.minimize(z3_dist((0, 0, 0), candidate))
    opt.check()

    model = opt.model()
    yield sum(abs(int(str(model[n]))) for n in candidate)


def z3_abs(x):
    """Returns the absolute value of x using Z3 conditional logic."""
    return If(x >= 0, x, -x)


def z3_dist(x, y):
    """Calculates the Manhattan distance between two points using Z3 solver constraints."""
    return Sum([If(a - b >= 0, a - b, b - a) for a, b in zip(x, y)])
