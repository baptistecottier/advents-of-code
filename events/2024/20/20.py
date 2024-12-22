from collections import deque

def preprocessing(puzzle_input):
    walls = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == '#':
                walls.add((x, y))
            if c == 'S': 
                start = (x, y)
            elif c == 'E':
                end = (x, y)
    return walls, start, end, x, y


def solver(walls: set, start , end, w, h):
    small_cheats = 0
    long_cheats = 0
    classical_path = bfs(walls, start, end)
    l = len(classical_path)
    for i, (xa, ya) in enumerate(classical_path):
        for j in range(i + 100, l):
            xb, yb = classical_path[j]
            m = abs(yb - ya) + abs(xb - xa)
            if (j - i - m >= 100):
                if m < 21: 
                    long_cheats += 1
                    if m < 3: small_cheats += 1
    yield small_cheats
    yield long_cheats
                
def bfs(walls, start, end):
    queue = deque([[start]])
    seen = set([start])
    
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (x2, y2) not in seen and (x2, y2) not in walls :
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))