"""
Advent of Code - Year 2018 - Day 18
https://adventofcode.com/2018/day/18
"""

from math import lcm
from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> tuple[
                                            set[tuple[int, int]],
                                            set[tuple[int, int]],
                                            set[tuple[int, int]]]:
    """
    Parses the puzzle input and returns sets of coordinates for grounds, trees, and lumberyards.

    Args:
        puzzle_input (str): The raw input string representing the landscape.

    Returns:
        tuple[set[tuple[int, int]], set[tuple[int, int]], set[tuple[int, int]]]:
            Sets of coordinates for grounds, trees, and lumberyards.
    """
    grounds = set()
    trees = set()
    lumberyards = set()

    for y, l in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(l):
            match c:
                case '.': grounds.add((x, y))
                case '|': trees.add((x, y))
                case '#': lumberyards.add((x, y))

    return grounds, trees, lumberyards


def solver(
    grounds: set[tuple[int, int]],
    trees: set[tuple[int, int]],
    lumberyards: set[tuple[int, int]]
) -> Iterator[int]:
    """
    Simulates the landscape evolution and yields the resource value at specific times.

    Args:
        grounds (set[tuple[int, int]]): Set of ground coordinates.
        trees (set[tuple[int, int]]): Set of tree coordinates.
        lumberyards (set[tuple[int, int]]): Set of lumberyard coordinates.

    Yields:
        int: The resource value (number of trees multiplied by number of lumberyards)
             at minute 10 and at the billionth minute.
    """
    seen_grounds = []
    seen_trees = []
    seen_lumberyards = []
    total_resources = []
    time = 0

    while any((
            grounds not in seen_grounds,
            trees not in seen_trees,
            lumberyards not in seen_lumberyards)
               ):
        seen_trees.append(trees)
        seen_grounds.append(grounds)
        seen_lumberyards.append(lumberyards)

        grounds, trees, lumberyards = update_landscape(grounds, trees, lumberyards)
        total_resources.append(len(trees) * len(lumberyards))
        time += 1
        if time == 10:
            yield len(trees) * len(lumberyards)

    shift = lcm(
        seen_trees.index(trees),
        seen_grounds.index(grounds),
        seen_lumberyards.index(lumberyards))

    period = len(seen_trees) - shift
    index = shift + ((1_000_000_000 - shift) % period) - 1
    yield total_resources[index]


def update_landscape(
    grounds: set[tuple[int, int]],
    trees: set[tuple[int, int]],
    lumberyards: set[tuple[int, int]]
) -> tuple[set[tuple[int, int]], set[tuple[int, int]], set[tuple[int, int]]]:
    """
    Updates the landscape for one minute according to the rules of the puzzle.

    Args:
        grounds (set[tuple[int, int]]): Set of ground coordinates.
        trees (set[tuple[int, int]]): Set of tree coordinates.
        lumberyards (set[tuple[int, int]]): Set of lumberyard coordinates.

    Returns:
        tuple[set[tuple[int, int]], set[tuple[int, int]], set[tuple[int, int]]]:
            Updated sets of coordinates for grounds, trees, and lumberyards.
    """
    updated_grounds = set()
    updated_trees = set()
    updated_lumberyards = set()
    neighbours = {(-1, 1),  (0, 1),  (1, 1),
                  (-1, 0),           (1, 0),
                  (-1, -1), (0, -1), (1, -1)}

    for (x, y) in grounds:
        if sum((x + dx, y + dy) in trees for dx, dy in neighbours) > 2:
            updated_trees.add((x, y))
        else:
            updated_grounds.add((x, y))

    for (x, y) in trees:
        if sum((x + dx, y + dy) in lumberyards for dx, dy in neighbours) > 2:
            updated_lumberyards.add((x, y))
        else:
            updated_trees.add((x, y))

    for (x, y) in lumberyards:
        if any((x + dx, y + dy) in trees for dx, dy in neighbours) and \
           any((x + dx, y + dy) in lumberyards for dx, dy in neighbours):
            updated_lumberyards.add((x, y))
        else:
            updated_grounds.add((x, y))

    return updated_grounds, updated_trees, updated_lumberyards
