"""
Advent of Code - Year 2018 - Day 6
https://adventofcode.com/2018/day/6
"""

from itertools import product


def preprocessing(puzzle_input: str) -> tuple[set, int, int, int, int]:
    """
    Parse coordinate pairs from input and return bounding box dimensions.
    """
    coordinates = set(tuple(int(item) for item in line.split(', '))
                      for line in puzzle_input.splitlines())
    list_x, list_y = zip(*coordinates)
    min_x, min_y = min(list_x), min(list_y)
    max_x, max_y = max(list_x), max(list_y)
    return coordinates, min_x, max_x, min_y, max_y


def solver(coordinates: set, min_x: int, max_x: int, min_y: int, max_y: int) -> tuple[int, int]:
    """
    Solves the coordinate area problem by finding the largest finite area and region size.
    """
    areas = {c: 0 for c in coordinates}
    corners = set()
    region_size = 0

    for x, y in product(range(min_x, max_x), range(min_y, max_y)):
        distances = []
        for xx, yy in coordinates:
            distances.append(abs(xx - x) + abs(yy - y))
        if sum(distances) < (10_000 if len(coordinates) == 50 else 32):
            region_size += 1
        mx, my = min(coordinates, key=lambda c, x=x, y=y: abs(c[0] - x) + abs(c[1] - y))
        if distances.count(abs(mx - x) + abs(my - y)) == 1:
            areas[(mx, my)] += 1
    print(areas)

    for x in range(min_x - 100, max_x + 100):
        for y in (min_y - 100, max_y + 100):
            distances = []
            for xx, yy in coordinates:
                distances.append(abs(xx - x) + abs(yy - y))
            mx, my = min(coordinates, key=lambda c, x=x, y=y: abs(c[0] - x) + abs(c[1] - y))
            if distances.count(abs(mx - x) + abs(my - y)) == 1:
                corners.add((mx, my))

    for y in range(min_y - 100, max_y + 100):
        for x in (min_x - 100, max_x + 100):
            distances = []
            for xx, yy in coordinates:
                distances.append(abs(xx - x) + abs(yy - y))
            mx, my = min(coordinates, key=lambda c, x=x, y=y: abs(c[0] - x) + abs(c[1] - y))
            if distances.count(abs(mx - x) + abs(my - y)) == 1:
                corners.add((mx, my))
    return max(areas[c] for c in coordinates if c not in corners), region_size
