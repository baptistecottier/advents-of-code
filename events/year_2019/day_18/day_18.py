"""
Advent of Code - Year 2019 - Day 18
https://adventofcode.com/2019/day/18
"""

from collections import deque
from copy import deepcopy


def preprocessing(puzzle_input: str) -> tuple[list[list[str]], tuple[int, int], int]:
    """
    Parses the puzzle input into a grid, the entrance coordinates, and the number of keys present.
    """
    entrance = (-1, -1)
    grid = []
    n_keys = len([c for c in puzzle_input if c.islower()])
    for y, line in enumerate(puzzle_input.splitlines()):
        if '@' in line:
            entrance = (line.index('@'), y)
        grid.append(list(line))
    return grid, entrance, n_keys


def solver(grid, entrance, n_keys):
    """
    Solves the shortest path to collect all keys in a grid-based puzzle, starting from the entrance,
    using BFS.
    """
    print(n_keys)
    print(entrance)
    queue = deque([([entrance], set())])
    while queue:
        path, keys = queue.popleft()
        go_back = len(path) < 2
        x, y = path[-1]
        # print(path)
        # print(keys)
        if grid[y][x].isupper():
            if grid[y][x].lower() not in keys:
                continue
        if grid[y][x].islower():
            keys.add(grid[y][x])
            go_back = True
            if len(keys) == n_keys:
                print(keys)
                print(len(path))
                print(path)
                yield len(path) - 1
        for tx, ty in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if grid[ty][tx] != '#' and (go_back or path[-2] != (tx, ty)):
                queue.append((path + [(tx, ty)], deepcopy(keys)))
