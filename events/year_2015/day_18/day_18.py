"""Advent of Code - Year 2015 - Day 18"""

from itertools import product
from dataclasses import dataclass, replace

@dataclass
class LightGrid:
    """
    LightGrid class to represent a grid of lights.

    Attributes:
        on (set): Set of coordinates representing lights that are on.
        w (int): Width of the grid.
        h (int): Height of the grid.
        always_on (set): Set of coordinates that are always on regardless of game rules.
    """
    on: set
    w: int
    h: int
    always_on: set

def preprocessing(puzzle_input: str) -> LightGrid:
    """
    Converts puzzle input string to a set of coordinates with active lights.

    Args:
        puzzle_input (str): String representing initial light configuration where '#' indicates on.

    Returns:
        tuple: (set of (x,y) coordinates of active lights, max x coordinate, max y coordinate)
    """
    lights_on = set()
    x, y = 0, 0
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == '#':
                lights_on.add((x, y))
    lights = LightGrid(lights_on, x, y, {(0, 0), (0, y), (y, 0), (x, y)})
    return lights


def solver(lights: LightGrid, iterations: int = 100):
    """
    Solve both parts of the puzzle.

    Args:
        lights: The initial light grid
        iterations: Number of iterations to run the simulation (default: 100)

    Yields:
        Part 1: Result after applying steps with corners off
        Part 2: Result after applying steps with corners always on
    """
    yield apply_steps(replace(lights, always_on = set()), iterations)
    yield apply_steps(lights, iterations)


def apply_steps(lights: LightGrid, iterations: int):
    """
    Apply game of life rules to the light grid for a given number of iterations.

    For each iteration, a light stays on if it has 2 or 3 neighbors that are on, 
    and turns on if it has exactly 3 neighbors that are on. Otherwise, it turns off.
    Lights in the `always_on` set remain on regardless of the rules.

    Args:
        lights: The LightGrid object containing the current state
        iterations: Number of iterations to perform

    Returns:
        int: The total number of lights that are on after all iterations
    """
    neighbours = {(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)}
    lights.on.update(lights.always_on)

    for _ in range(iterations):
        updated_lights = lights.always_on.copy()
        for (x, y) in product(range(lights.w + 1), range(lights.h + 1)):
            match sum((x + dx, y + dy) in lights.on for (dx, dy) in neighbours):
                case 3:
                    updated_lights.add((x, y))
                case 2:
                    if (x, y) in lights.on:
                        updated_lights.add((x, y))
        lights.on = updated_lights
    return len(lights.on)
