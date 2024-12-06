"""
Preprocessing consists in retrieving all obstacles and the guard position
"""
def preprocessing(puzzle_input):
    obstacles = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == '^': 
                guard = (x, y)
            elif c == '#': 
                obstacles.add((x, y))
    return (guard, obstacles, x, y)


"""
Solver simply compute in a first time the length of the patrol before the guard gets
out of map. Then for each spot the guard visits, we simulate the new patrol if an
obstacle where placed there, and count how many of them results in a loop
"""
def solver(guard, obstacles: set, x, y):
    honest_patrol = patrol(guard, obstacles, x, y)
    yield len(honest_patrol)
    
    n_good_obstacles = 0
    for obstacle in honest_patrol:
        new_obstacles = obstacles.copy()
        new_obstacles.add(obstacle)
        if patrol(guard, new_obstacles, x, y) == set():
            n_good_obstacles +=1
    yield n_good_obstacles


"""
Patrol simulate the path made by the guard during its patrol. While an obstacle is met,
the guard keeps turning 90 degrees to the right. When the guard is out of the map, the
path is returned. If the guard loops, an empty path is returned
"""    
def patrol(guard, obstacles, x, y):
    gx, gy = guard
    dx, dy = (0, -1)
    visited = set()
    while 0 <= gx <= x and 0 <= gy <= y:
        if ((dx, dy), (gx, gy)) in visited: 
                return set()
        visited.add(((dx, dy), (gx, gy)))
        while (gx + dx, gy + dy) in obstacles:
            dx, dy = (dy if dx else - dy, dx)
        gx, gy = gx + dx, gy + dy
    return set(pt for (_, pt) in visited)