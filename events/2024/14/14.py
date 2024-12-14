from pythonfw.functions import extract_chunks, sign
from math               import prod


def preprocessing(puzzle_input): 
    """
    Capture all numbers and return chunk of 4 numbers corrsponding to 
    px, py, vx and vy
    """
    return extract_chunks(puzzle_input, 4)


def solver(robots, w = 101, h = 103):
    """
    Until less than 100 seconds have elapsed and the christmas tree have been found
    once, we simulate the movements of the robots. A double agent elve told us the
    tree need a space which is more than 30 tiles wide and tall to be displayed.
    """
    seconds = 1
    found = (w < 30 or h < 30)
    while seconds <= 100 or not found:
        new_robots = list()
        columns = {y: 0 for y in range(h)}
        rows = {x: 0 for x in range(w)}
        for px, py, vx, vy in robots:
            px = (px + vx) % w
            py = (py + vy) % h
            new_robots.append((px, py, vx, vy))
            rows[px]    += 1
            columns[py] += 1
        if not found:
            if max(rows.values())    > 30 and \
               max(columns.values()) > 30:
                yield seconds
                found = True
        robots = new_robots
        if seconds == 100: 
            yield safety_factor(robots, w, h)
        seconds += 1


def safety_factor(robots, w = 101, h = 103):
    """
    Given a list of robots, we sort them according to the quadrant they belong to.
    """
    quadrants = {(-1, -1): 0, (1, -1): 0, (-1, 1): 0, (1, 1): 0}
    for x, y, _, _ in robots:
        if x != (w // 2) and y != (h // 2):
            quadrants[sign(x, w // 2), sign(y, h // 2)] += 1
    return prod(quadrants.values())

