from re                 import findall
from pythonfw.functions import extract_chunks
from pythonfw.classes   import Point
from parse import parse
from collections import deque

def preprocessing(puzzle_input):
    clay = set()
    for line in puzzle_input.splitlines():
        axis, a, _, b, c = list(parse("{}={:d}, {}={:d}..{:d}", line))
        for m in range(b, c + 1):
            clay.add((a, m) if axis == 'x' else (m, a))
    return clay

def solver(clay: set):

    max_y = min(y for _, y in clay)
    min_x = min(x for x, _ in clay)
    max_x = max(x for x, _ in clay)
    clay.intersection_update({(tx, max_y + 1) for tx in range(min_x - 1, max_x + 1)})

    start = (500, 0)
    queue = deque([[start]])
    seen = set([start])

    while queue: 
        path = queue.popleft()
        x, y = path[-1]
        if y > max_y: continue
        if (x, y + 1) not in clay: 
            while (x, y + 1) not in clay: y += 1
            queue.append(path + [(x, y + 1)])
        else:
            if (x - 1, y) not in clay:


