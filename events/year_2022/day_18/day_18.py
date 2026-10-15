"""
Advent of Code - Year 2022 - Day 18
https://adventofcode.com/2022/day/18
"""

# Standard imports
from collections import deque
from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> set[tuple[int, ...]]:
    """
    Converts the comma-separated coordinates of each cube into a set of tuples.
    """
    droplet = set()
    for line in puzzle_input.splitlines():
        droplet.add(tuple(map(int, line.split(','))))
    return droplet


def solver(droplet: set[tuple[int, ...]]) -> Iterator[int]:
    """
    Yields the surface area of the droplet, i.e. the faces of its cubes not touching another
    cube, then its exterior surface area, i.e. the faces reached by the steam.
    """
    steam = fill(droplet)
    faces = 6 * len(droplet)
    cnt_droplet = 0
    cnt_steam = 0
    for (x, y, z) in droplet:
        for node in (
             (x, y, z - 1), (x, y - 1, z), (x - 1, y, z),
             (x, y, z + 1), (x, y + 1, z), (x + 1, y, z)):
            if node in droplet:
                cnt_droplet += 1
            if node in steam:
                cnt_steam += 1
    yield faces - cnt_droplet
    yield cnt_steam


def fill(droplet: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
    """
    Fills the air around the droplet with steam, starting from a corner of its bounding box
    enlarged by one cube on each side so that the steam can flow all around the droplet.
    Returns the cubes reached by the steam: air pockets enclosed in the droplet are left out.
    """
    min_x = min(x for x, _, _ in droplet) - 1
    min_y = min(y for _, y, _ in droplet) - 1
    min_z = min(z for _, _, z in droplet) - 1
    max_x = max(x for x, _, _ in droplet) + 1
    max_y = max(y for _, y, _ in droplet) + 1
    max_z = max(z for _, _, z in droplet) + 1

    queue = deque([(min_x, min_y, min_z)])
    steam = set()
    while queue:
        x, y, z = queue.pop()
        for tx, ty, tz in (
                (x, y, z - 1), (x, y - 1, z), (x - 1, y, z),
                (x, y, z + 1), (x, y + 1, z), (x + 1, y, z)):
            if (tx, ty, tz) in droplet or (tx, ty, tz) in steam:
                continue
            if tx not in range(min_x, max_x + 1):
                continue
            if ty not in range(min_y, max_y + 1):
                continue
            if tz not in range(min_z, max_z + 1):
                continue
            queue.append((tx, ty, tz))
        steam.add((x, y, z))
    return steam
