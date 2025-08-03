"""
Advent of Code - Year 2018 - Day 11
https://adventofcode.com/2018/day/11
"""

from collections.abc import Iterator
from itertools import product


def preprocessing(puzzle_input: str) -> int:
    """Converts the puzzle input string to an integer."""
    return int(puzzle_input)


def solver(serial: int) -> Iterator[str]:
    """
    Finds optimal fuel cell grid coordinates for maximum power.

    Args:
        serial: Grid serial number for power calculation

    Yields:
        str: "x,y" coordinates for 3x3 grid with max power
        str: "x,y,size" coordinates and size for any grid with max power

    Examples:
        >>> list(solver(18))
        ['33,45', '90,269,16']
        >>> list(solver(42))
        ['21,61', '232,251,12']
    """

    def p(x: int, y: int):
        return x * (x * y + serial) // 100 % 10 - 5

    grid = [[p(x, y) for x in range(11, 311)] for y in range(1, 301)]
    width = 1
    m, x, y = maximum_power(grid, width)
    max_infos = (x, y, 1)
    max_power = m

    while m:
        width += 1
        m, x, y = maximum_power(grid, width)
        if width == 3:
            yield f"{x},{y}"
        if m > max_power:
            max_power = m
            max_infos = (x, y, width)

    yield ",".join(str(n) for n in max_infos)


def maximum_power(grid: list[list[int]], width: int) -> tuple[int, int, int]:
    """
    Find the top-left coordinates and maximum power sum for a square subgrid of given width.
    """
    max_score = 0
    mx, my = (-1, -1)
    for x, y in product(range(300 - width), repeat=2):
        score = sum(sum(grid[y + yy][x: x + width]) for yy in range(width))
        if score > max_score:
            max_score, mx, my = score, x + 1, y + 1
    return max_score, mx, my
