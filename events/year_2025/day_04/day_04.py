"""
Advent of Code - Year 2025 - Day 4
https://adventofcode.com/2025/day/4
"""


def preprocessing(puzzle_input: str) -> set[tuple[int, int]]:
    """
    Parse puzzle input and return the set of coordinates where '@' characters are found.
    """
    roll = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == '@':
                roll.add((x, y))

    return roll


def solver(rolls: set[tuple[int, int]]) -> tuple[int, int]:
    """
    Iteratively removes positions with fewer than 4 neighbors until no more can be removed.
    Returns the count removed in the first iteration and the total count removed.
    """
    removed = [1, -1]  # Set as it to pass the while predicate while not modifying the final sum
    neighbours = ((-1, -1), (0, -1), (1, -1),
                  (-1, 0),           (1, 0),
                  (-1, 1),  (0, 1),  (1, 1))
    while removed[-1] != 0:
        to_remove = {(rx, ry) for rx, ry in rolls
                     if sum((rx + dx, ry + dy) in rolls for (dx, dy) in neighbours) < 4}
        removed.append(len(to_remove))
        rolls = rolls.difference(to_remove)

    return removed[2], sum(removed)
