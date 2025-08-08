# pylint: skip-file
# flake8: noqa
# type: ignore

"""
Advent of Code - Year 2023 - Day 23
https://adventofcode.com/2023/day/23
"""

from collections import deque
from copy import deepcopy

def preprocessing(puzzle_input):
    grid = [list(line) for line in puzzle_input.splitlines()]
    return grid


def solver(grid):
    intersections = {}
    start = (1, 0)
    h = len(grid)
    w = len(grid[0])
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if grid[y][x] == '#':
                continue
            cnt = 0
            for x2, y2 in ((x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)):
                if grid[y2][x2] != '#':
                    cnt += 1
            if cnt > 2:
                intersections[(x, y)] = False
    end = (len(grid[-1]) - 2, len(grid) - 1)
    queue = deque([([start], deepcopy(intersections))])
    slope = {'<': (-1, 0), '>': (1, 0), 'v': (0, 1), '^': (0, -1)}
    max_length = 0
    while queue:
        path, intersections = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            max_length = max(max_length, len(path) - 1)
        for x2, y2 in ((x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)):
            if len(path) > 1 and (x2, y2) == path[-2]:
                continue
            if w > x2 > 0 and h > y2 > 0:
                if grid[y2][x2] == '.':
                    if (x2, y2) in intersections:
                        if intersections[(x2, y2)] is False:
                            temp_inter = intersections.copy()
                            temp_inter[(x2, y2)] = True
                            queue.append((path + [(x2, y2)], temp_inter))
                    else:
                        queue.append((path + [(x2, y2)], intersections))
                        
                if grid[y2][x2] in "<>v^":
                    if (x2 - x, y2 - y) == slope[grid[y2][x2]]:
                        queue.append((path + [(x2, y2)], intersections))
    yield max_length