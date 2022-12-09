import numpy as np 

def generator(input) :
    x, y = 0, 0
    path = [[x,y]]
    for dir, step in [ins.split(' ') for ins in input.splitlines()]:
        match dir :
            case 'D' : (dx, dy) = (0, -1)
            case 'L' : (dx, dy) = (-1, 0)
            case 'R' : (dx, dy) = (1, 0)
            case 'U' : (dx, dy) = (0, 1)
        for _ in range(int(step)):
            x , y = x + dx , y + dy
            path.append([x,y])
    return path
            
def part_1(input) :
    return solver(input, 2)

def part_2(input) :
    return solver(input, 10)

def solver(path, knots) :
    for _ in range(knots-1):
        tx , ty = 0 , 0
        visited = []
        for [hx, hy] in path :
            d = abs(hy  - ty) > 1 or abs(hx - tx) > 1
            tx += d * np.sign(hx - tx)
            ty += d * np.sign(hy - ty)
            visited.append([tx, ty])
        path = visited
        
    return len([list(x) for x in set(tuple(x) for x in visited)])