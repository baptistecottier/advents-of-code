import re 
from math import lcm

def generator(input):
    data = [int(item) for item in re.findall('[+-]?\d+', input)]
    scan = tuple(tuple(data[i::3]) for i in range(4))
    return scan
    
def part_1(input):
    scans = tuple(apply_motion(input[dim], 1_000) for dim in range(3))
    return sum(sum(abs(scans[i][0][j]) for i in range(3)) * sum(abs(scans[i][1][j]) for i in range(3)) for j in range(4))
    
def part_2(input):
    return lcm(*[apply_motion(input[dim]) for dim in range(3)])
        
    
def apply_motion(scans, rounds = -1):
    gravity = (0, 0, 0, 0)
    visited = set()
    r = -1
    while (r := r + 1) != rounds:
        if (scans, gravity) in visited: return r
        else : visited.add((scans, gravity))
        gravity = tuple(g + sum(sign(p, q) for q in scans) for g, p in zip(gravity,scans))
        scans = tuple((p + g) for p, g in zip(scans, gravity))
    return scans, gravity

def sign(a, b): return (a < b) - (a > b)
