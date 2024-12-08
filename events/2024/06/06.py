"""
Preprocessing consists in retrieving all obstacles location and the guard position.
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
Solver computes the length of the path made by the guard. For each step, a
simulation of the patrol with an osbtacle in place of the next step is run,
to determine if this obstruction leads the guard to loop, or not. The final
length of the visited place is the answer to part 1, while the number of
obstacle leading to a looping patrol answers part 2.
"""
def solver(guard, obstacles, width, heigh):
    obstructions = set()
    gx, gy = guard
    dx, dy = (0, -1)
    visited = set()
    while 0 <= gx <= width and 0 <= gy <= heigh:
        while (gx + dx, gy + dy) in obstacles:
            dx, dy = (dy if dx else - dy, dx)
        obstacle = (gx + dx, gy + dy)
        # As an optimization we may make the guard starts at the actual 
        # position, except if the next point has already been met before
        if obstacle in visited:
            start = (guard, ((0, -1)))
        else:
            start = ((gx, gy), (dx, dy))
        if is_patrol_looping(start, obstacles.union([obstacle]), width, heigh):
            obstructions.add(obstacle)
        visited.add(((gx, gy)))
        gx, gy = obstacle
    yield len(visited)
    yield len(obstructions)


"""
is_patrol_looping determines if a patrol loops given a set of obstacles. Either
a guard ends his patrol outside of the map, either he ends it looping. Hence, 
if a place is visited twice with the same orientation (dx, dy), we deduce the
guard loops.
"""    
def is_patrol_looping(start, obstacles, width, heigh):
    (gx, gy), (dx, dy) = start
    visited = set()
    while 0 <= gx <= width and 0 <= gy <= heigh:
        if ((dx, dy), (gx, gy)) in visited: 
                return True
        visited.add(((dx, dy), (gx, gy)))
        while (gx + dx, gy + dy) in obstacles:
            dx, dy = (dy if dx else - dy, dx)
        gx, gy = gx + dx, gy + dy
    return False
        

