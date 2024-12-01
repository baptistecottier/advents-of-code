from collections import defaultdict
from math import atan, degrees

def preprocessing(puzzle_input):
    belt = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, asteroid in enumerate(line):
            if asteroid == '#': belt.add((x, y))
    return belt
    
def solver(puzzle_input):
    asteroids = {}
    for (x, y) in puzzle_input:
        angles = defaultdict(list)
        
        for (xx, yy) in puzzle_input:
            if (xx, yy) == (x, y): continue
            dx, dy = xx - x, yy - y
            div = (dx ** 2 + dy ** 2) ** (0.5)
            if dx + div != 0: angle = round(degrees(2 * atan(dy/(dx + div))), 5)
            else: angle = 180
            angles[(90 + angle) % 360].append((xx,yy))
            
        if len(angles.keys()) > len(asteroids.keys()): 
            (bx, by), asteroids = (x, y), angles
    yield len(asteroids)
    
    try:
        distances = {(cx, cy): abs(cx - bx)+abs(cy - by) for cx, cy in sorted(asteroids.items())[199][1]}
        (x, y) = min(distances.keys(), key = lambda c: distances[c])
        yield 100 * x + y
    except:
        yield None