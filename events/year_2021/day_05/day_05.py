"""
Advent of Code - Year 2021 - Day 5
https://adventofcode.com/2021/day/5
"""

from collections import defaultdict
from pythonfw.functions import extract_chunks, sign


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Converts the puzzle input string into a list of lists of integers by extracting chunks of
    size 4.
    """
    return extract_chunks(puzzle_input, 4)


def solver(vents: list[list[int]]) -> tuple[int, int]:
    """
    Counts the number of points where at least two horizontal/vertical or any lines overlap in a
    list of vents.
    """
    visited = defaultdict(int)
    diagonal = defaultdict(int)

    for (sx, sy, ex, ey) in vents:
        if sx == ex:
            for pos in ((sx, y) for y in range(min(sy, ey), 1 + max(sy, ey))):
                visited[pos] += 1
        elif sy == ey:
            for pos in ((x, sy) for x in range(min(sx, ex), 1 + max(sx, ex))):
                visited[pos] += 1
        else:
            dx, dy = sign(ex - sx), sign(ey - sy)
            for pos in ((sx + k * dx, sy + k * dy) for k in range(abs(sx - ex) + 1)):
                diagonal[pos] += 1

    keys = set(visited.keys()).union(diagonal.keys())
    return (sum(visited.get(k, 0) > 1 for k in keys),
            sum((visited.get(k, 0) + diagonal.get(k, 0)) > 1 for k in keys))
