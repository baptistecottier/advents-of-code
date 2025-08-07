# type: ignore
# pylint: skip-file
# flake8: noqa

"""
Advent of Code - Year 2022 - Day 24
https://adventofcode.com/2022/day/24
"""

def preprocessing(puzzle_input):
    walls = set()
    blizzards = defaultdict(set)
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            match c:
                case '#': walls.add((x, y))
                case '>': blizzards[(x, y)].add((1, 0))
                case 'v': blizzards[(x, y)].add((0, 1))
                case '<': blizzards[(x, y)].add((-1, 0))
                case '^': blizzards[(x, y)].add((0, -1))
                case '.': 
                    if y == 0: start = x
                    else: end = x
    return walls, blizzards, start, (end, y), x

from collections import deque
def solver(walls, blizzards, start, end, w):
    _, h = end
    queue = deque([[(start, 0)]])
    seen = set([(start, 0)])
    len_path = 1
    blizzards = update(blizzards, h, w)
    while queue:
        moved = False
        path = queue.popleft()
        print(path)
        if len(path) == len_path + 1:
            blizzards = update(blizzards, h, w)
            # print(blizzards)
            len_path += 1
            print(len_path)
        x, y = path[-1]
        if (x, y) == end:
            print(path)
            yield len(path) - 1
            break
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (x2, y2) not in blizzards.keys() and (x2, y2) not in walls and y2 >= 0 and x2 >= 0:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
                moved = True
        if not moved: queue.append(path + [(x, y)])


from collections import defaultdict
def update(blizzards, h, w):

    print('#' * (w + 1))
    for dy in range(1, h):
        line = "#"
        for dx in range(1, w):
            if (dx, dy) not in blizzards.keys():
                line += "."
            elif len(blizzards[(dx, dy)]) > 1: 
                line += str(len(blizzards[(dx, dy)]))
            else:
                a, b = blizzards[(dx, dy)].pop()
                line += {(1, 0): '>', (-1, 0): '<', (0, 1): 'v', (0, -1): '^'}[(a, b)]
                blizzards[(dx, dy)].add((a, b))
        print(line+"#")
    print('#' * (w + 1))
    new = defaultdict(set)
    for (x, y), v in blizzards.items():
        for dx, dy in v:
            tx = x + dx
            if tx > (w - 1): tx = 1
            if tx < 1 : tx = w - 1
            ty = (y + dy)
            if ty > (h - 1): ty = 1
            if ty < 1: ty = h - 1
            new[(tx, ty)].add((dx, dy))
    return new

