"""
Advent of Code - Year 2023 - Day 18
https://adventofcode.com/2023/day/18
"""

from shapely import Polygon


def preprocessing(puzzle_input: str) -> list[Polygon]:
    """
    Returns polygons formed by each instructions parameters.
    """
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    instructions = [[(0, 0)], [(0, 0)]]
    for line in puzzle_input.splitlines():
        d1, n1, h = line.split(' ')

        # Proceed with first approach
        dx = (1, 0, -1, 0)["RDLU".index(d1)]
        dy = (0, 1, 0, -1)["RDLU".index(d1)]
        n1 = int(n1)
        x1, y1 = x1 + n1 * dx, y1 + n1 * dy
        instructions[0].append((x1, y1))

        # Proceed with second approach
        d2 = int(h[-2]) % 4
        dx = (1, 0, -1, 0)[d2]
        dy = (0, 1, 0, -1)[d2]
        n2 = int(h[2:-2], 16)
        x2, y2 = x2 + n2 * dx, y2 + n2 * dy
        instructions[1].append((x2, y2))
    instructions[0].append((0, 0))
    instructions[1].append((0, 0))
    return [
        Polygon(instructions[0]),
        Polygon(instructions[1])
    ]


def solver(polygons: list[Polygon]):
    """
    Compute the number of cubic meters of lava the lagoon could hold using the Pick's
    theorem.
    """
    for poly in polygons:
        yield int(poly.length // 2 + poly.area) + 1
