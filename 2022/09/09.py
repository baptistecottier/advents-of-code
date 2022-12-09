import numpy as np 

def generator(input) :
    x, y = 0, 0
    path = [[x,y]]
    orientation = {'D' : (0, -1) , 'L' : (-1, 0) ,  'R' : (1, 0), 'U' : (0, 1)}
    for dir, step in [ins.split(' ') for ins in input.splitlines()]:
        (dx , dy) = orientation[dir]
        path.append((x + i * dx , y + i * dy) for i in range(int(step)))
        (x , y) =(x + step * dx, y + step * dy)
    return path
            
def part_1(input) :
    return solver(input, 2)

def part_2(input) :
    return solver(input, 10)

def solver(path, knots) :
    for _ in range(knots-1):
        tx , ty = 0 , 0
        visited = []
        for (hx, hy) in path :
            d = abs(hy  - ty) > 1 or abs(hx - tx) > 1
            tx += d * np.sign(hx - tx)
            ty += d * np.sign(hy - ty)
            visited.append((tx, ty))
        path = visited
        
    return len([list(x) for x in set(tuple(x) for x in visited)])