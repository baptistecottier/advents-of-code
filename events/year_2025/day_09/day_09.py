"""
Advent of Code - Year 2025 - Day 9
https://adventofcode.com/2025/day/9
"""

from itertools import combinations
from shapely import Polygon


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Parse puzzle input to extract coordinates and return them as a sorted list of tuples.
    """
    red_tiles = set()
    for line in puzzle_input.splitlines():
        (x, y) = tuple(map(int, line.split(',')))
        red_tiles.add((x, y))
    return sorted(red_tiles)


def solver(red_tiles: list) -> tuple[int, int]:
    """
    Calculates the largest rectangle area that can be formed from a set of red tiles,
    distinguishing between rectangles fully contained within the main shape and those that are not.
    """
    areas = {True: 0, False: 0}
    geometries = []
    to_connect = red_tiles.copy()

    while to_connect:
        pt_a = to_connect.pop()
        coords = [pt_a]
        found = True
        while found:
            found = False
            for pt_b in to_connect:
                if pt_a[0] == pt_b[0] or pt_a[1] == pt_b[1]:
                    to_connect.remove(pt_b)
                    coords.append(pt_b)
                    pt_a = pt_b
                    found = True
                    break
        geometries.append(Polygon(coords))

    geometries = sorted(geometries, key=lambda g: g.area, reverse=True)
    main_shape = geometries[0]

    for hole in geometries[1:]:
        main_shape = main_shape.difference(hole)

    for ((xa, ya), (xb, yb)) in combinations(red_tiles, 2):
        is_contained = main_shape.contains(Polygon(((xb, yb), (xa, yb), (xa, ya), (xb, ya))))
        areas[is_contained] = max(
            areas[is_contained],
            (abs(xb - xa) + 1) * (1 + abs(yb - ya)))

    return max(areas.values()), areas[True]
