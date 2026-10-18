"""
Advent of Code - Year 2019 - Day 24
https://adventofcode.com/2019/day/24
"""


from collections import defaultdict
from itertools import product


def preprocessing(puzzle_input):
    """
    Parses the input grid into the set of (x, y) coordinates of the tiles containing a bug.
    """
    bugs = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, b in enumerate(line):
            if b == '#':
                bugs.add((x, y))
    return bugs


def solver(bugs):
    """
    Evolves the bugs minute by minute until a layout appears twice, and yields the biodiversity
    rating of that layout, then the number of bugs on the recursive levels after 200 minutes.
    """
    visited = set()
    b2 = bugs.copy()
    n = state_to_int(bugs)
    while n not in visited:
        visited.add(n)
        new = set()
        for x in range(5):
            for y in range(5):
                infested = sum(((x + a, y + b) in bugs)
                               for (a, b)
                               in [(-1, 0), (1, 0), (0, -1), (0, 1)])
                if infested == 1 or ((x, y) not in bugs and infested == 2):
                    new.add((x, y))
        bugs = new.copy()
        n = state_to_int(bugs)
    yield state_to_int(bugs)
    yield part_2(b2)


def state_to_int(state):
    """
    Encodes a set of bug coordinates as an integer whose bit x + 5 * y is set for each bug, which
    is also its biodiversity rating.
    """
    n = 0
    for x, y in state:
        n += 2 ** (x + 5 * y)
    return n


def int_to_state(n):
    """
    Decodes an integer produced by state_to_int back into the set of bug coordinates.
    """
    bugs = set()
    for i in range(25):
        if (n >> i) & 1:
            bugs.add((i % 5, i // 5))
    return bugs


# A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
# An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.

def part_2(bugs):
    """
    Evolves the bugs for 200 minutes over the recursive levels, starting from the input at depth
    0, and returns the total number of bugs.
    """
    depths = defaultdict(set)
    depths[0] = bugs
    for _ in range(200):
        new_depth = defaultdict(set)
        levels = depths.keys()
        for d in range(min(levels) - 1, max(levels) + 2):
            b = depths[d]
            for (x, y) in product(range(5), range(5)):
                if x == y == 2:
                    continue
                score = sum((nx, ny) in depths[nd] for (nd, nx, ny) in neighbors(d, x, y))
                if score == 1 or (score == 2 and (x, y) not in b):
                    new_depth[d].add((x, y))
        depths = new_depth
    print(depths)
    return sum(len(b) for b in depths.values())


def neighbors(d, x, y):  # pylint: disable=too-many-return-statements,too-many-branches
    """
    Returns the (depth, x, y) coordinates of the tiles adjacent to tile (x, y) of depth d, where
    depth d + 1 is the grid surrounding depth d and depth d - 1 the grid inside its centre.
    """
    # 1, 2, 3, 4, 5, 6, 7, 9, 11, 16, 17, 19, 21, 22, 23, 24, 25

    if (x, y) in ((1, 1), (1, 3), (3, 1), (3, 3)):
        return ((d, tx, ty) for tx, ty in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))

    if y == 0 and x in (1, 2, 3):
        return ((d, x - 1, y), (d, x + 1, y), (d, x, y + 1), (d + 1, 2, 1))

    if y == 4 and x in (1, 2, 3):
        return ((d, x - 1, y), (d, x + 1, y), (d, x, y - 1), (d + 1, 2, 3))

    if x == 0 and y in (1, 2, 3):
        return ((d, x, y - 1), (d, x, y + 1), (d, x + 1, y), (d + 1, 1, 2))

    if x == 4 and y in (1, 2, 3):
        return ((d, x, y - 1), (d, x, y + 1), (d, x - 1, y), (d + 1, 3, 2))

    match (x, y):
        case (0, 0):
            return ((d, 1, 0), (d, 0, 1), (d + 1, 2, 1), (d + 1, 1, 2))
        case (4, 0):
            return ((d, 3, 0), (d, 4, 1), (d + 1, 2, 1), (d + 1, 3, 2))
        case (0, 4):
            return ((d, 0, 3), (d, 1, 4), (d + 1, 2, 3), (d + 1, 1, 2))
        case (4, 4):
            return ((d, 3, 4), (d, 4, 3), (d + 1, 2, 3), (d + 1, 3, 2))
        case (2, 1):
            return ((d, 1, 1), (d, 2, 0), (d, 3, 1),
                    (d - 1, 0, 0), (d - 1, 1, 0), (d - 1, 2, 0), (d - 1, 3, 0), (d - 1, 4, 0))
        case (1, 2):
            return ((d, 1, 1), (d, 0, 2), (d, 1, 3),
                    (d - 1, 0, 0), (d - 1, 0, 1), (d - 1, 0, 2), (d - 1, 0, 3), (d - 1, 0, 4))
        case (3, 2):
            return ((d, 3, 1), (d, 4, 2), (d, 3, 3),
                    (d - 1, 4, 0), (d - 1, 4, 1), (d - 1, 4, 2), (d - 1, 4, 3), (d - 1, 4, 4))
        case (2, 3):
            return ((d, 1, 3), (d, 2, 4), (d, 3, 3),
                    (d - 1, 0, 4), (d - 1, 1, 4), (d - 1, 2, 4), (d - 1, 3, 4), (d - 1, 4, 4))
    raise ValueError(f"({x}, {y}) is the centre of the grid, not a tile")
