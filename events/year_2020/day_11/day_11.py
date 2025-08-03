"""
Advent of Code - Year 2020 - Day 11
https://adventofcode.com/2020/day/11
"""

from collections.abc import Iterator
from copy import deepcopy
from itertools import product


def preprocessing(puzzle_input: str) -> list[list[str]]:
    """
    Converts a multiline string input into a 2D list of characters, padding each row and column
    with '.' to avoid further IndexErrors
    """
    rows = puzzle_input.splitlines()
    width = len(rows[0]) + 2
    seats = [list('.' * (width))] + [list(f".{row}.") for row in rows] + [list('.' * (width))]

    return seats


def solver(boat: list[list[str]]) -> Iterator[int]:
    """
    Yields the total number of seats with value 2 after organizing the seating arrangement with and
    without an extra range.
    """
    for extra_range in (False, True):
        stable_boat = organise_boat(boat, extra_range)
        yield sum(sum(boat == '#' for boat in row) for row in stable_boat)


def organise_boat(boat: list[list[str]], extra_range: bool) -> list[list[str]]:
    """
    Iteratively applies seating rules to the boat layout until it stabilizes and returns the final
    arrangement.
    """
    updated_boat = apply_rules(boat, extra_range)
    while boat != updated_boat:
        boat = updated_boat
        updated_boat = apply_rules(boat, extra_range)
    return updated_boat


def apply_rules(boat: list[list[str]], extra_range: bool) -> list[list[str]]:
    """
    Applies seating rules to a 2D grid representing a boat, updating seat states based on adjacent
    or visible neighbors depending on the extra_range flag.
    """
    updated_boat = deepcopy(boat)
    height = len(boat)
    width = len(updated_boat[0])
    neighbours = {(-1, -1), (-1, 0), (-1, 1),
                  (0,  -1),          (0,  1),
                  (1,  -1), (1,  0), (1,  1)}

    for x, y in product(range(1, width), range(1, height)):
        in_sight = []
        for dx, dy in neighbours:
            x2, y2 = x + dx, y + dy
            if extra_range:
                while y2 in range(height) and x2 in range(width) and boat[y2][x2] == '.':
                    x2, y2 = x2 + dx, y2 + dy
            if y2 in range(height) and x2 in range(width):
                in_sight.append((y2, x2))

        match boat[y][x]:
            case 'L':
                if all(boat[y2][x2] != '#' for y2, x2 in in_sight):
                    updated_boat[y][x] = '#'
            case '#':
                if sum(boat[y2][x2] == '#' for y2, x2 in in_sight) >= (4 + extra_range):
                    updated_boat[y][x] = 'L'

    return updated_boat
