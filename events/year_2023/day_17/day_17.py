# pylint: skip-file
# flake8: noqa
# type: ignore

"""
Advent of Code - Year 2023 - Day 17
https://adventofcode.com/2023/day/17
"""

from collections import deque, defaultdict


def preprocessing(puzzle_input):
    return [[int(item) for item in line] for line in puzzle_input.splitlines()]


def solver(grid):
    queue = deque([[(0, 0, 0, 1,  0, 0)]])
    size = 12
    min_loss = sum(sum(loss for loss in line) for line in grid)
    # min_loss = sum(grid[x][x]+grid[x][x + 1] for x in range(size)) + grid[size][size]
    print(min_loss)
    loss_pos = defaultdict(lambda: min_loss)
    while queue:
        path = queue.pop()
        x, y, dx, dy, loss, blocks = path[-1]
        if loss > min_loss:
            continue
        if (x, y) == (size, size):
            if loss < min_loss:
                min_loss = loss
            print(min_loss)
        else:
            if blocks < 3:
                try:
                    if (x + dx) >= 0 and (y + dy) >= 0 and loss_pos[(x + dx, y + dy)] >= (grid[y + dy][x + dx] + loss):
                        loss_pos[(x + dx, y + dy)] = grid[y + dy][x + dx] + loss
                        queue.append(path + [(x + dx, y + dy, dx, dy, loss + grid[y + dy][x + dx], blocks + 1)])
                except:
                    pass
            try:
                    if (x - dy) >= 0 and (y + dx) >= 0 and loss_pos[(x - dy, y + dx)] >= (grid[y + dx][x - dy] + loss):
                        loss_pos[(x - dy, y + dx)] = grid[y + dx][x - dy] + loss
                        queue.append(path + [(x - dy, y + dx, -dy, dx, loss + grid[y + dx][x - dy], 1)])
            except:
                pass
            try:
                    if (x + dy) >= 0 and (y - dx)>= 0 and loss_pos[(x + dy, y - dx)] >=  (grid[y - dx][x + dy] + loss):
                        loss_pos[(x + dy, y - dx)] = grid[y - dx][x + dy] + loss
                        queue.append(path + [(x + dy, y - dx, dy, -dx, loss + grid[y - dx][x + dy], 1)])
            except:
                pass
    yield min_loss
