from collections import defaultdict
from math import atan, degrees

def generator(input):
    belt = set()
    for y, line in enumerate(input.splitlines()):
        for x, asteroid in enumerate(line):
            if asteroid == '#': belt.add((x, y))
    return belt

def part_1(input):
    return len(solver(input)[1])

def part_2(input): 
    (bx, by), asteroids = solver(input)
    distances = {(cx, cy): abs(cx - bx)+abs(cy - by) for cx, cy in sorted(asteroids.items())[199][1]}
    (x, y) = min(distances.keys(), key = lambda c : distances[c])
    return 100 * x + y
    
def solver(input):
    max_angles = {}
    for (x, y) in input:
        angles = defaultdict(list)
        
        for (xx, yy) in input:
            dx, dy = xx - x, yy - y
            div = (dx ** 2 + dy ** 2) ** (0.5)
            if dx + div != 0 : angle = round(degrees(2 * atan(dy/(dx + div))), 5)
            else: angle = 180
            angles[(90 + angle) % 360].append((xx,yy))
            
        if len(angles.keys()) > len(max_angles.keys()): 
            (bx, by), max_angles = (x, y), angles
    return (bx, by), max_angles