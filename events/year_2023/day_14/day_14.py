"""
Advent of Code - Year 2023 - Day 14
https://adventofcode.com/2023/day/14
"""


def preprocessing(puzzle_input: str) -> tuple[set[tuple[int, int]], set[tuple[int, int]], int, int]:
    """
    Parses the puzzle input and returns sets of round and square rock positions along with grid
    width and height.
    """
    rounded = set()
    cube = set()
    height = puzzle_input.count('\n') + 1
    x = 0
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            match c:
                case 'O': rounded.add((x, height - y))
                case '#': cube.add((x, height - y))
    return rounded, cube, x + 1, height


def solver(rounded: set[tuple[int, int]], cube: set[tuple[int, int]], w: int, h: int):
    """
    Simulates tilting operations on a grid and yields the sum of y-coordinates after each cycle,
    detecting cycles to efficiently compute future states.
    """
    loads = []
    rounded = tilt_n(rounded, cube, h)
    yield sum(y for _, y in rounded)

    rounded = tilt_w(rounded, cube)
    rounded = tilt_s(rounded, cube)
    rounded = tilt_e(rounded, cube, w)
    loads.append(sorted(rounded))

    while True:
        rounded = tilt_n(rounded, cube, h)
        rounded = tilt_w(rounded, cube)
        rounded = tilt_s(rounded, cube)
        rounded = tilt_e(rounded, cube, w)

        if rounded not in loads:
            loads.append(rounded)
        else:
            stt = loads.index(rounded)
            prd = len(loads) - stt
            idx = stt + (1_000_000_000 - stt) % prd - 1
            yield sum(y for _, y in loads[idx])
            break


def tilt_n(rounded: set[tuple[int, int]], cube: set[tuple[int, int]], h: int
           ) -> set[tuple[int, int]]:
    """
    Tilts round objects downward within a grid until they hit a square or another tilted object.
    """
    tlt = set()
    for x, y in rounded:

        while (x, y) not in cube and y <= h:
            y += 1
        y -= 1

        while (x, y) in tlt:
            y -= 1
        tlt.add((x, y))

    return tlt


def tilt_w(rounded: set[tuple[int, int]], cube: set[tuple[int, int]]
           ) -> set[tuple[int, int]]:
    """
    Tilts all rounded rocks westward until they hit a cube or the edge, returning their new
    positions.
    """
    tlt = set()
    for x, y in rounded:

        while (x, y) not in cube and x >= 0:
            x -= 1
        x += 1

        while (x, y) in tlt:
            x += 1
        tlt.add((x, y))

    return tlt


def tilt_s(rounded: set[tuple[int, int]], cube: set[tuple[int, int]]
           ) -> set[tuple[int, int]]:
    """
    Tilts rounded objects southwards until they hit a cube or another rounded object, returning
    their new positions.
    """
    tlt = set()
    for x, y in rounded:

        while (x, y) not in cube and y > 0:
            y -= 1
        y += 1

        while (x, y) in tlt:
            y += 1
        tlt.add((x, y))

    return tlt


def tilt_e(rounded: set[tuple[int, int]], cube: set[tuple[int, int]], w: int
           ) -> set[tuple[int, int]]:
    """
    Tilts a set of round objects eastward within a grid, stopping at squares or the grid's edge.
    """
    tlt = set()
    for x, y in rounded:

        while (x, y) not in cube and x < w:
            x += 1
        x -= 1

        while (x, y) in tlt:
            x -= 1
        tlt.add((x, y))

    return tlt
