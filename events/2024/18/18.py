from collections import deque

def preprocessing(puzzle_input):
    """
    Simply retrieves the coordinates of the falling kilobytes.
    """
    falls = list()
    for coord in puzzle_input.splitlines():
        x, y = coord.split(',')
        falls.append((int(x), int(y)))
    return falls


def solver(falls, size = 70, delay = 1024):
    """
    Run a Breadth First Search algorithm to find the shortest path from the starting
    point to the ending point for the first part. For the first part, we apply
    dichotomies on the delay of fallen kilobytes using a BFS algorithm to determine
    if a path does still exist, and updates bounds according to the result. When
    right = left + 1, this means a path exist when stoping after left kilobytes 
    falls, but no path exists after right kilobytes falls
    """
    yield bfs(falls[:delay], size)
    
    left = delay
    right = len(falls)
    while right - left > 1:
        if bfs(falls[:(left + right) // 2], size) != -1:
            left = (left + right) // 2
        else:
            right = (left + right) // 2
    x, y = falls[left]
    yield f"{x},{y}"


def bfs(maze, size):
    queue = deque([[(0, 0)]])
    seen = set([(0, 0)])
    
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == (size, size):
            return len(path)-1
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (x2, y2) not in seen and (x2, y2) not in maze and 0 <= x2 <= size and 0 <= y2 <= size:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return -1
