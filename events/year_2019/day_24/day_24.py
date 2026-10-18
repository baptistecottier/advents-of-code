"""
Advent of Code - Year 2019 - Day 24
https://adventofcode.com/2019/day/24
"""


from collections import defaultdict
from collections.abc import Iterator
from itertools import product


def preprocessing(puzzle_input: str) -> set[tuple[int, int]]:
    """
    Parses the input grid into the set of (x, y) coordinates of the tiles containing a bug.
    """
    bugs: set[tuple[int, int]] = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(line):
            if char == '#':
                bugs.add((x, y))
    return bugs


def solver(bugs: set[tuple[int, int]]) -> Iterator[int]:
    """
    Yields the biodiversity rating of the first layout that appears twice, then the number of bugs
    on the recursive levels after 200 minutes.
    """
    yield first_repeated_rating(bugs)
    yield sum(len(level_bugs) for level_bugs in simulate_n_minutes(bugs, 200).values())


def has_bug_next(adjacent: int, has_bug: bool) -> bool:
    """
    Tells whether a tile holds a bug after one minute, given its number of adjacent bugs and
    whether it holds one now: a bug survives with exactly one adjacent bug, and an empty tile gets
    infested with one or two.
    """
    return adjacent == 1 or (adjacent == 2 and not has_bug)


def first_repeated_rating(bugs: set[tuple[int, int]]) -> int:
    """
    Evolves the bugs minute by minute until a layout appears twice, and returns the biodiversity
    rating of that layout.
    """
    visited: set[int] = set()
    n = state_to_int(bugs)
    while n not in visited:
        visited.add(n)
        new: set[tuple[int, int]] = set()
        for (x, y) in product(range(5), range(5)):
            adjacent = sum((x + dx, y + dy) in bugs
                           for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)])
            if has_bug_next(adjacent, (x, y) in bugs):
                new.add((x, y))
        bugs = new
        n = state_to_int(bugs)
    return n


def state_to_int(state: set[tuple[int, int]]) -> int:
    """
    Encodes a set of bug coordinates as an integer whose bit x + 5 * y is set for each bug, which
    is also its biodiversity rating.
    """
    n = 0
    for x, y in state:
        n += 2 ** (x + 5 * y)
    return n


def simulate_n_minutes(bugs: set[tuple[int, int]], n: int) -> dict[int, set[tuple[int, int]]]:
    """
    Evolves the bugs for n minutes over the recursive levels, starting from the given bugs at
    depth 0, and returns the bugs of each depth.
    """
    depths: defaultdict[int, set[tuple[int, int]]] = defaultdict(set)
    depths[0] = bugs
    for _ in range(n):
        new_depth: defaultdict[int, set[tuple[int, int]]] = defaultdict(set)
        levels = depths.keys()
        for d in range(min(levels) - 1, max(levels) + 2):
            level_bugs = depths[d]
            for (x, y) in product(range(5), range(5)):
                if x == y == 2:
                    continue
                adjacent = sum((nx, ny) in depths[nd]
                               for (nd, nx, ny) in recursive_neighbours(d, x, y))
                if has_bug_next(adjacent, (x, y) in level_bugs):
                    new_depth[d].add((x, y))
        depths = new_depth
    return depths


def recursive_neighbours(d: int, x: int, y: int) -> tuple[tuple[int, int, int], ...]:
    """
    Returns the (depth, x, y) coordinates of the tiles adjacent to tile (x, y) of depth d, where
    depth d + 1 is the grid surrounding depth d and depth d - 1 the grid inside its centre. The
    centre itself is not a tile and has none.
    """
    neighbours: tuple[tuple[int, int, int], ...] = ()

    if (x, y) in ((1, 1), (1, 3), (3, 1), (3, 3)):
        neighbours = ((d, x + 1, y), (d, x - 1, y), (d, x, y + 1), (d, x, y - 1))

    elif y == 0 and x in (1, 2, 3):
        neighbours = ((d, x - 1, y), (d, x + 1, y), (d, x, y + 1), (d + 1, 2, 1))

    elif y == 4 and x in (1, 2, 3):
        neighbours = ((d, x - 1, y), (d, x + 1, y), (d, x, y - 1), (d + 1, 2, 3))

    elif x == 0 and y in (1, 2, 3):
        neighbours = ((d, x, y - 1), (d, x, y + 1), (d, x + 1, y), (d + 1, 1, 2))

    elif x == 4 and y in (1, 2, 3):
        neighbours = ((d, x, y - 1), (d, x, y + 1), (d, x - 1, y), (d + 1, 3, 2))

    elif y == 0 and x in (0, 4):
        dx = 0 if x == 0 else 2
        neighbours = ((d, 1 + dx, 0), (d, x, 1), (d + 1, 2, 1), (d + 1, 1 + dx, 2))

    elif y == 4 and x in (0, 4):
        dx = 0 if x == 0 else 2
        neighbours = ((d, 1 + dx, 4), (d, x, 3), (d + 1, 2, 3), (d + 1, 1 + dx, 2))

    elif y == 2 and x in (1, 3):
        nx = 0 if x == 1 else 4
        neighbours = ((d, x, 1), (d, nx, 2), (d, x, 3), (d - 1, nx, 0),
                      (d - 1, nx, 1), (d - 1, nx, 2), (d - 1, nx, 3), (d - 1, nx, 4))

    elif x == 2 and y in (1, 3):
        ny = 0 if y == 1 else 4
        neighbours = ((d, 1, y), (d, 2, ny), (d, 3, y), (d - 1, 0, ny),
                      (d - 1, 1, ny), (d - 1, 2, ny), (d - 1, 3, ny), (d - 1, 4, ny))

    return neighbours
