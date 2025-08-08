# pylint: skip-file
# flake8: noqa
# type: ignore

"""
Advent of Code - Year 2023 - Day 18
https://adventofcode.com/2023/day/18
"""

def preprocessing(puzzle_input): 
    x, y = 0, 0
    board = set()
    for line in puzzle_input.splitlines():
        print(line)
        d, n, h = line.split(' ')
        match h[-2]: 
            case '0' : dx, dy = 1, 0
            case '2' : dx, dy = -1, 0
            case '3' : dx, dy = 0, -1
            case '1' : dx, dy = 0, 1
        for _ in range(int(h[2:-2], 16)):
            x, y = x + dx, y + dy
            board.add((x, y))
    return board
from collections import deque

def fill(maze, start):
    queue = deque([[start]])
    seen = set([start])
    
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (x2, y2) not in seen and (x2, y2) not in maze:
                queue.append((x2, y2))
                seen.add((x2, y2))
    return len(seen)

def solver(board):
    yield len(board) + fill(board, (1, 1))

