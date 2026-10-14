"""
Advent of Code - Year 2019 - Day 18
https://adventofcode.com/2019/day/18
"""

from collections import deque
from collections.abc import Iterator
from copy import deepcopy


def preprocessing(puzzle_input: str) -> tuple[list[list[str]], tuple[int, int], int]:
    """
    Parses the puzzle input into a grid, the entrance coordinates, and the number of keys present.
    """
    puzzle_input = """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""
    entrance = (-1, -1)
    grid = []
    n_keys = len([c for c in puzzle_input if c.islower()])
    for y, line in enumerate(puzzle_input.splitlines()):
        if '@' in line:
            entrance = (line.index('@'), y)
        grid.append(list(line))
    return grid, entrance, n_keys


def solver(grid: list[list[str]], entrance: tuple[int, int], n_keys: int) -> Iterator[int]:
    """
    Solves the shortest path to collect all keys in a grid-based puzzle, starting from the entrance,
    using BFS.
    """
    queue = deque([([entrance], set())])
    keys = set()
    visited = [(entrance, keys)]
    while queue:
        path, keys = queue.popleft()
        print(queue)
        x, y = path[-1]
        go_back = False
        if grid[y][x].isupper():
            if grid[y][x].lower() not in keys:
                continue
            if len(keys) == n_keys:
                yield len(path) - 1
            else:
                grid[y][x] = '.'
        elif grid[y][x].islower():
            keys.add(grid[y][x])
            go_back = True
            if len(keys) == n_keys:
                yield len(path) - 1
        visited.append(((x, y), keys))
        for tx, ty in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if grid[ty][tx] != '#' and ((tx, ty), keys) not in visited:
                if len(path) >= 2 and (tx, ty) == path[-2] and not go_back:
                    continue
                queue.append((path + [(tx, ty)], keys.copy()))
