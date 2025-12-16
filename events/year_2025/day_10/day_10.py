"""
Advent of Code - Year 2025 - Day 10
https://adventofcode.com/2025/day/10
"""


from itertools import combinations
from scipy.optimize import linprog

import numpy as np


def preprocessing(puzzle_input: str) -> list[tuple]:
    """
    Extract machines information (indicator lights diagram (ild), button wiring schematics (bws)
    and joltage requirements (jm)) from the puzzle input.
    """
    machines = []
    for line in puzzle_input.splitlines():
        data = line.split(' ')
        ild = [int(c == '#') for c in data[0][1:-1]]
        bws = []
        for d in data[1:-1]:
            bws.append([int(c) for c in d[1:-1].split(',')])
        jr = [int(c) for c in data[-1][1:-1].split(',')]
        machines.append([ild, bws, jr])
    return machines


def solver(machines: list[tuple]) -> tuple[int, int]:
    """
    Firstly compute the fewest button presses required to correctly configure the indicator lights
    on all of the machines. As two presses on a button has no effect, we know no more than one
    press by button will be required. Then computes the fewest button presses required to correctly
    configure the joltage level counters on all of the machines using linear programming.
    """
    fewest_presses_for_lights = 0
    fewest_presses_for_joltage = 0

    for ild, buttons, joltage in machines:
        found = False
        size = 0
        while not found:
            size += 1
            for comb in combinations(buttons, size):
                lights = [0 for _ in range(len(ild))]
                for button in comb:
                    lights = [1 - l if n in button else l for n, l in enumerate(lights)]
                if lights == ild:
                    found = True
                    break
        fewest_presses_for_lights += size

        mtrx = [[0 for _ in range(len(buttons))] for _ in range(len(joltage))]
        for x, button in enumerate(buttons):
            for y in button:
                mtrx[y][x] = 1
        n_presses = find_smallest_solution(mtrx, joltage)
        fewest_presses_for_joltage += n_presses

    return fewest_presses_for_lights, fewest_presses_for_joltage


def find_smallest_solution(matrix_a: list[list[int]], vector_b: list[int]):
    """
    Finds the smallest number of button presses to achieve the required joltage using linear
    programming to solve the system.
    """
    n = len(matrix_a[0])
    np_b = np.array(vector_b, dtype=int)
    np_a = np.array(matrix_a, dtype=int)
    a_ub = np.vstack([np_a, -np_a])
    b_ub = np.hstack([np_b, -np_b])
    c = np.ones(n)
    integrality = [1 for _ in range(n)]
    res = linprog(c, A_ub=a_ub, b_ub=b_ub, integrality=integrality)
    return int(res.x.sum())
