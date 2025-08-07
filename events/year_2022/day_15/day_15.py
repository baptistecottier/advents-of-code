"""
Advent of Code - Year 2022 - Day 15
https://adventofcode.com/2022/day/15
"""

# Standard imports
from collections.abc import Iterator
from itertools import chain, product

# First party imports
from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input: str) -> set[tuple[int, int, int]]:
    """
    Processes the puzzle input string and returns a set of sensor tuples containing coordinates and
    Manhattan distances.
    """
    sensors = extract_chunks(puzzle_input, 4)
    sensors = {(xs, ys, abs(xb - xs) + abs(yb - ys)) for xs, ys, xb, yb in sensors}
    return sensors


def solver(sensors: set[tuple[int, int, int]], max_size: int = 4_000_000) -> Iterator[int]:
    """
    Yields the number of unique x-coordinates covered by the sensors and the first position not
    covered by any sensor in a grid of given size.
    """
    cnt = set()

    for xs, ys, md in sensors:
        cnt.add(range(xs - (md - abs(ys - max_size // 2)),
                      1 + xs + (md - abs(ys - max_size // 2))))
    yield len(set(list(chain.from_iterable(cnt)))) - 1

    for x, y in product(range(0, max_size), repeat=2):
        if all((abs(xs - x) + abs(ys - y)) > md for xs, ys, md in sensors):
            yield 4_000_000 * x + y
            break
