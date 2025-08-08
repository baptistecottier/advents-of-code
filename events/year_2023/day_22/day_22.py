"""
Advent of Code - Year 2023 - Day 22
https://adventofcode.com/2023/day/22
"""

from collections import defaultdict
from collections.abc import Iterator
from itertools import product


def preprocessing(puzzle_input: str) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    """
    Parses the puzzle input string into a sorted list of brick coordinate tuples.
    """
    bricks = []
    puzzle_input = puzzle_input.replace('~', ',')
    for line in puzzle_input.splitlines():
        xa, ya, za, xb, yb, zb = list(map(int, line.split(',')))
        bricks.append(((xa, ya, za), (xb, yb, zb)))
    return sorted(bricks, key=lambda b: b[0][2])


def solver(bricks: list[tuple[tuple[int, int, int], tuple[int, int, int]]]) -> Iterator[int]:
    """
    Solves the brick support puzzle by calculating the number of removable bricks and the total
    number of bricks that would fall if each removable brick is removed.
    """
    support = drop_bricks(bricks)
    to_keep = set()
    for _, v in support.items():
        if len(v) == 1:
            to_keep.add(list(v)[0])
    yield len(bricks) - len(to_keep)

    total_falling = 0
    for n in to_keep:
        falling = set([n])
        for k, v in support.items():
            if v.issubset(falling):
                falling.add(k)
        total_falling += len(falling)
    yield total_falling - len(to_keep)


def drop_bricks(bricks: list[tuple[tuple[int, int, int], tuple[int, int, int]]]
                ) -> dict[int, set[int]]:
    """
    Simulates dropping bricks onto a surface and returns a mapping of each brick to the set of
    bricks it is supported by.
    """
    rest = set()
    support = defaultdict(set)
    locations = {}
    for n, ((xa, ya, za), (xb, yb, zb)) in enumerate(bricks):
        cubes = set()
        for x, y, z in product(range(min(xa, xb), max(xa, xb) + 1),
                               range(min(ya, yb), max(ya, yb) + 1),
                               range(min(za, zb), max(za, zb) + 1)):
            cubes.add((x, y, z))

        while (min(z for (_, _, z) in cubes) != 1 and
               not any((x, y, z - 1) in rest for (x, y, z) in cubes)):
            cubes = {(x, y, z - 1) for (x, y, z) in cubes}
        rest.update(cubes)

        for (x, y, z) in cubes:
            locations[(x, y, z)] = n
            if (x, y, z - 1) not in cubes and (x, y, z - 1) in locations:
                support[n].add(locations[(x, y, z - 1)])

    return support
