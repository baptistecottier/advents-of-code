from collections import deque

def bfs(maze, start , end, max_length = None):
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if len(path) - 2 == max_length : 
            return None
        if (x , y) == end:
            return len(path) - 1
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if  (x2, y2) in maze and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
