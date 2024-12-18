from collections import deque

def preprocessing(puzzle_input):
    falls = list()
    for coord in puzzle_input.splitlines():
        x, y = coord.split(',')
        falls.append((int(x), int(y)))
    return falls

def solver(falls):
    SIZE = 70
    delay = 1024
    yield bfs(falls[:delay], SIZE)
    
    a = delay
    b = len(falls)
    while b - a > 1:
        if bfs(falls[:(a + b) // 2], SIZE) != -1:
            a = (a + b) // 2
        else:
            b = (a + b) // 2
    x, y = falls[a]
    yield f"{x},{y}"


def bfs(maze, SIZE):
    queue = deque([[(0, 0)]])
    seen = set([(0, 0)])
    
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == (SIZE, SIZE):
            return len(path)-1
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (x2, y2) not in seen and (x2, y2) not in maze and 0 <= x2 <= SIZE and 0 <= y2 <= SIZE:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return -1
