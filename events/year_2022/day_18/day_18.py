"""
Advent of Code - Year 2022 - Day 18
https://adventofcode.com/2022/day/18
"""

# Standard imports
from collections.abc import Iterator

# First party imports
from pythonfw.classes import Point


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Converts a comma-separated string input into a list of lists of integers.
    """
    droplet = []
    for line in puzzle_input.splitlines():
        droplet.append(list(map(int, line.split(','))))
    return droplet


def solver(droplet: list[list[int]]) -> Iterator[int]:
    """
    Calculates and yields the surface area of a 3D droplet represented as a list of coordinate
    triplets.
    """
    cnt = 0
    for i, a in enumerate(droplet):
        for b in droplet[i+1:]:
            if any(
                    a[n % 3] == b[n % 3] and
                    a[(n + 1) % 3] == b[(n + 1) % 3] and
                    abs(a[(n + 2) % 3] - b[(n + 2) % 3]) == 1
                    for n in range(3)):
                cnt += 1

    yield 6 * len(droplet) - 2 * cnt


def part_2(droplet: list[list[int]]) -> None:
    """
    Calculates and the list of air pockets within the bounding box of a droplet structure.
    """
    max_x = max(a[0] for a in droplet)
    max_y = max(a[1] for a in droplet)
    max_z = max(a[2] for a in droplet)
    min_x = min(a[0] for a in droplet)
    min_y = min(a[1] for a in droplet)
    min_z = min(a[2] for a in droplet)
    pt_min = Point(min_x, min_y, min_z)
    pt_max = Point(max_x, max_y, max_z)
    steam = []
    air = []
    fill((0, 0, 0), pt_min, pt_max, droplet, steam)
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            for z in range(min_z, max_z):
                if [x, y, z] not in steam and [x, y, z] not in droplet:
                    air.append([x, y, z])
    print("air:", air)


def fill(pos: tuple[int, int, int],
         pt_min: Point,
         pt_max: Point,
         droplet: list[list[int]],
         steam: list[tuple[int, int, int]]):
    """
    Recursively fills a 3D space starting from a given position, marking visited positions in
    'steam' and avoiding positions in 'droplet' within specified bounds.
    """
    steam.append(pos)
    print(pos)
    if pos in droplet or pos in steam:
        return

    [x, y, z] = pos
    if z-1 > pt_min.z:
        fill((x, y, z-1), pt_min, pt_max, droplet, steam)
    if z+1 < pt_max.z:
        fill((x, y, z+1), pt_min, pt_max, droplet, steam)
    if y-1 > pt_min.y:
        fill((x, y-1, z), pt_min, pt_max, droplet, steam)
    if y+1 < pt_max.y:
        fill((x, y+1, z), pt_min, pt_max, droplet, steam)
    if x-1 > pt_min.x:
        fill((x-1, y, z), pt_min, pt_max, droplet, steam)
    if x+1 < pt_max.x:
        fill((x+1, y, z), pt_min, pt_max, droplet, steam)
    return
