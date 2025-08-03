"""
Advent of Code - Year 2020 - Day 17
https://adventofcode.com/2020/day/17
"""

from itertools import product


def preprocessing(puzzle_input: str) -> tuple[set[tuple[int, ...]], int]:
    """
    Parses the input string to extract the coordinates of activated cubes and computes the grid
    size.
    """
    activated = set()
    size = len(puzzle_input.splitlines()) // 2
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, cube in enumerate(line):
            if cube == '#':
                activated.add((x - size, y - size))
    return activated, size


def solver(activated: set[tuple[int, ...]], size: int):
    """
    Yields the result of booting up a grid of given size and initial activated cells in 3 and 4
    dimensions.
    """
    for dimension in [3, 4]:
        yield boot_up(activated, size, dimension)


def boot_up(activated: set[tuple[int, ...]], size: int, dimension: int) -> int:
    """
    Simulates a 3D or higher-dimensional cellular automaton for six cycles and returns the number
    of active cells at the end.
    """
    activated = {(x, y) + (0,) * (dimension - 2) for (x, y) in activated}
    neighbours = [deltas for deltas in product(range(-1, 2), repeat=dimension)
                  if any(item != 0 for item in deltas)]

    for _ in range(6):
        size += 1
        new_activated = set()

        for coord in product(range(- size, size + 1), repeat=dimension):
            nb = [tuple(t + dt for t, dt in zip(coord, delta)) for delta in neighbours]
            score = sum(n in activated for n in nb)
            if score == 3 or (score == 2 and coord in activated):
                new_activated.add(coord)
        activated = new_activated

    return len(activated)
