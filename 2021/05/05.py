from parse import parse
from numpy import sign

def generator(input): 
    return [tuple(parse('{:d},{:d} -> {:d},{:d}', line)) for line in input.splitlines()]

def part_1(input): 
    return solver(input, False)

def part_2(input): 
    return solver(input, True)

def solver(vents, diagonal):
    visited, points = {}, {}
    for (sx, sy, ex, ey) in vents:
        if sx == ex: points = ((sx, y) for y in range(min(sy, ey), 1 + max(sy, ey)))
        elif sy == ey: points = ((x, sy) for x in range(min(sx, ex), 1 + max(sx, ex)))
        elif diagonal : 
            dx, dy = sign(ex - sx), sign(ey - sy)
            points = ((sx + k * dx, sy + k * dy) for k in range(abs(sx - ex) + 1))
        for (x, y) in points:
            if (x, y) in visited: visited[(x, y)] += 1
            else : visited[(x, y)] = 1
    return sum(item > 1 for item in visited.values())