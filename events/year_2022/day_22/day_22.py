# type: ignore
# pylint: skip-file
# flake8: noqa

"""
Advent of Code - Year 2022 - Day 22
https://adventofcode.com/2022/day/22
"""

import re


def preprocessing(puzzle_input: str):
    board, raw_path = puzzle_input.split('\n\n')

    tiles = set()
    walls = set()
    for y, line in enumerate(board.splitlines()):
        for x, c in enumerate(line):
            if c == '.':
                tiles.add((x, y))
            elif c == '#':
                walls.add((x, y))
    dx, dy = turn_left((1, 0))
    path = []   
    print("R" + raw_path)
    for t, n in re.findall("(L|R)(\d+)", "R" + raw_path):
        if t == 'L':
            dx, dy = turn_left((dx, dy))
            path.append((int(n), (dx, dy)))
        else:
            dx, dy = turn_right((dx, dy))
            path.append((int(n), (dx, dy)))
    return tiles, walls, path


def turn_left(dir):
    match dir: 
        case (n, 0): return (0, -n)
        case (0, n): return (n, 0)

def turn_right(dir):
    match dir: 
        case (n, 0): return (0, n)
        case (0, n): return (-n, 0)


def solver(tiles, walls, path):
    both = walls.union(tiles)
    x, y = min(tiles, key=lambda x: (x[1], x[0]))
    dx = dy = 0
    for n, (dx, dy) in path:
        for _ in range(n):
            if (x + dx, y + dy) in walls:
                continue
            if (x + dx, y + dy) not in tiles:
                match dx, dy:
                    case 1, 0:
                        tx = min(a for a, b in both if b == y)
                        if (tx, y) not in walls:
                            x = tx
                    case -1, 0:
                        tx = max(a for a, b in both if b == y)
                        if (tx, y) not in walls:
                            x = tx
                    case 0, 1:
                        ty = min(b for a, b in both if a == x)
                        if (x, ty) not in walls:
                            y = ty
                    case 0, -1:
                        ty = max(b for a, b in both if a == x)
                        if (x, ty) not in walls:
                            y = ty
            else:
                x += dx
                y += dy

    facing = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}
    yield 1_000 * (y + 1) + 4 * (x + 1) + facing[(dx, dy)]
