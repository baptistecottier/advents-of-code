"""Advent of Code - Year 2015 - Day 18"""

from dataclasses import dataclass, replace
from itertools   import product

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


def solver(lights: LightGrid, iterations: int = 100) -> tuple[int, int]:
    """
    Solve the puzzle by calculating the number of lights that are on after a given number of 
    iterations.

    Parameters:
        lights (LightGrid): The initial grid of lights.
        iterations (int, optional): The number of iterations to apply. Defaults to 100.

    Returns:
        tuple[int, int]: A tuple containing:
            - Part 1: Number of lights on after iterations without any always-on corners
            - Part 2: Number of lights on after iterations with the original grid

    Examples:
        >>> grid = LightGrid({(0, 0), (0, 1), (1, 0)}, 3, 3)
        >>> solver(grid, 4)
        (4, 7)
    """
    return (apply_steps(replace(lights, always_on = set()), iterations),
            apply_steps(lights, iterations))


def apply_steps(lights: LightGrid, iterations: int) -> int:
    """
    Applies the Game of Life rules to a light grid for a given number of iterations.
    
    Args:
        lights: A LightGrid object containing the current state of lights
        iterations: The number of iterations to simulate
    
    Returns:
        int: The number of lights that are on after all iterations
        
    Example:
        >>> grid = LightGrid(width=5, height=5)
        >>> grid.on = {(1, 1), (2, 2), (3, 3)}
        >>> apply_steps(grid, 4)
        0
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
