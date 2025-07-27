"""
Advent of Code - Year 2017 - Day 22
https://adventofcode.com/2017/day/22
"""

# Standard imports
from collections import defaultdict
from copy import deepcopy

# First-party imports
from pythonfw.classes import Particule2D


def preprocessing(puzzle_input: str) -> tuple[defaultdict[tuple[int, int], float], Particule2D]:
    """
    Parse the puzzle input into a set of infected nodes and determine grid size.

    Args:
        puzzle_input (str): The puzzle input as a string, representing a grid.

    Returns:
        tuple: A pair containing:
            - list of tuples: Coordinates (x, y) of infected nodes
            - int: Size of the grid
    """
    x = y = 0
    states = defaultdict(float)
    grid = puzzle_input.splitlines()
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            states[(x, y)] = float(c == '#')
    return states, Particule2D((x // 2, y // 2), (0, -1))


def solver(states: defaultdict[tuple[int, int], float], carrier: Particule2D) -> tuple[int, int]:
    """
    Solves the virus infection problem for part 1 and part 2 using the burst function.
    """
    return (burst(deepcopy(states), deepcopy(carrier), False),
            burst(states, carrier, True))


def burst(states: defaultdict[tuple[int, int], float], carrier: Particule2D, evolved: bool) -> int:
    """
    Simulates virus carrier bursts on a grid with infection states.

    Args:
        states: Dictionary mapping (x,y) positions to infection states
        carrier: Particle that moves and rotates on the grid
        evolved: if True, uses 4-state model with 10M bursts;
                 if False, uses 2-state model with 10K bursts

    Returns:
        int: Number of nodes that became infected during simulation
    """
    if evolved:
        n_bursts = 10_000_000
        step = .5
    else:
        n_bursts = 10_000
        step = 1

    cnt = 0

    for _ in range(n_bursts):
        pos = carrier.xy()
        state = states[pos]
        match state:
            case 0:
                carrier.rotate_left()
            case 1:
                carrier.rotate_right()
            case 1.5:
                carrier.reverse()

        if state + step == 1:
            cnt += 1

        states[pos] = (state + step) % 2
        carrier.move()

    return cnt
