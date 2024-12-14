from pythonfw.functions import extract_chunks, sign
from math               import prod


def preprocessing(puzzle_input): 
    """
    Capture all numbers and return chunk of 4 numbers respectively corrsponding to 
    px, py, vx and vy
    """
    return extract_chunks(puzzle_input, 4)


def solver(robots, w = 101, h = 103):
    """
    Until less than 100 seconds have elapsed and the christmas tree have been found
    once, we simulate the movements of the robots. A double agent elf told us the
    tree need a space which is more than 31 tiles wide and 33 tiles tall to be 
    displayed.
    """
    seconds = 1
    found = (w < 31 or h < 33)
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
            if max(rows.values())    > 31 and \
               max(columns.values()) > 33:
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

