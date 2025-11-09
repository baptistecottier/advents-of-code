"""
Advent of Code - Year 2021 - Day 17
https://adventofcode.com/2021/day/17
"""

# Standard imports
from re import findall
from itertools import product

# First party import
from pythonfw.classes import Particule
from pythonfw.functions import sign


def preprocessing(puzzle_input: str) -> tuple[int, ...]:
    """
    Extracts and returns a tuple of integers representing the target area from the puzzle input
    string.
    """
    target = tuple(map(int, findall(r'[-]?[0-9]+', puzzle_input)))
    return target


def solver(tx_min: int, tx_max: int, ty_min: int, ty_max: int) -> tuple[int, int]:
    """
    Simulates projectile motion to find the highest y-position and the number of initial velocities
    that land within the target area.
    """

    global_max_y = 0
    good_init_velo = 0

    for vx, vy in product(range(tx_max + 1), range(ty_min, -ty_min)):
        pos = Particule(0, 0, 0, vx + sign(vx), vy + 1, 0, 0, -1, 0)
        max_y = 0
        while pos.p.x <= tx_max and pos.p.y >= ty_min:
            pos.move()
            pos.v.x -= sign(pos.v.x)
            max_y = max(max_y, pos.p.y)

            if (tx_min <= pos.p.x <= tx_max) and (ty_min <= pos.p.y <= ty_max):
                good_init_velo += 1
                global_max_y = max(global_max_y, max_y)
                break

    return global_max_y, good_init_velo
