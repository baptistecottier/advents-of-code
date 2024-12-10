from collections import deque, defaultdict

def preprocessing(puzzle_input):
    topographic_map = []
    starts = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        longitude = []
        for x, c in enumerate(line):
            if c == '0': starts.add((x, y))
            longitude.append(int(c))
        topographic_map.append(longitude)
    return topographic_map, starts, x, y
            

def solver(topo_map, starts, width, height):
    reachable_points = 0
    distinct_trails = 0
    for (x, y) in starts:
        hiking_trails = explore_map(topo_map, (x, y), width, height)
        reachable_points +=len(hiking_trails.keys())
        distinct_trails += sum(ht for ht in hiking_trails.values())
    yield reachable_points
    yield distinct_trails


def explore_map(maze, start, width, height):    
    ongoing_trails = deque([start])  
    hiking_trails = defaultdict(int)
    while ongoing_trails:
        x, y = ongoing_trails.popleft()
        if maze[y][x] == 9:
            hiking_trails[(x, y)] += 1
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (0 <= x2 <= width and 0 <= y2 <= height):
                if maze[y2][x2] == maze[y][x] + 1:
                    ongoing_trails.append((x2, y2))
    return hiking_trails