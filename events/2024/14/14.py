from pythonfw.functions import extract_chunks, sign
from math               import prod

def preprocessing(puzzle_input): 
    return extract_chunks(puzzle_input, 4)

def solver(robots, w = 101, h = 103):
    seconds = 1
    found = w < 30
    while seconds <= 100 or not found:
        new_robots = set()
        columns = {y: 0 for y in range(h)}
        rows = {x: 0 for x in range(w)}
        for px, py, vx, vy in robots:
            px = (px + vx) % w
            py = (py + vy) % h
            new_robots.add((px, py, vx, vy))
            columns[py] += 1
            rows[px] += 1
        if not found:
            if max(rows.values()) >= w // 3 and \
               max(columns.values()) >= h // 3:
                yield seconds
                found = True
        robots = new_robots
        if seconds == 100: 
            yield safety_factor(robots, w, h)
        seconds += 1

def safety_factor(robots, w = 101, h = 103):
    quadrants = {(-1, -1): 0, (1, -1): 0, (-1, 1): 0, (1, 1): 0}
    for x, y, _, _ in robots:
        if x != (w // 2) and y != (h // 2):
            quadrants[sign(x, w // 2), sign(y, h // 2)] += 1
    return prod(quadrants.values())

