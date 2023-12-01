def preprocessing(input_): 
    grid = []
    for line in input_.splitlines(): 
        grid.append([int(item) for item in line.split(',')])
    
    return grid 

import itertools 

def solver(input_): 
    cnt = 0
    for i, a in enumerate(input_): 
        for j, b in enumerate(input_[i+1:]):
            if  any(a[n % 3] == b[n % 3] \
                    and a[(n + 1) % 3] == b[(n + 1) % 3]\
                    and abs(a[(n + 2) % 3] - b[(n + 2) % 3]) == 1 \
                for n in range(3)): cnt += 1
        
    yield 6 * len(input_) - 2 * cnt

def part_2(input_): 
    max_x = max([a[0] for a in input_])
    max_y = max([a[1] for a in input_])
    max_z = max([a[2] for a in input_])
    min_x = min([a[0] for a in input_])
    min_y = min([a[1] for a in input_])
    min_z = min([a[2] for a in input_])
    steam = []
    air = []
    fill([0,0,0], min_x, max_x, min_y, max_y, min_z, max_z, input_, steam)
    for x in range(min_x, max_x): 
        for y in range(min_y, max_y): 
            for z in range(min_z, max_z): 
                if [x, y, z] not in steam and [x, y, z] not in input_: air.append([x,y,z])
    print("air:", air)

def fill(pos, xmin, xmax, ymin, ymax, zmin, zmax, input_, steam):
    steam.append(pos)
    print(pos)
    if pos in input_ or pos in steam: 
        return
    else: 
        [x, y, z] = pos
        if z-1 > zmin: fill([x, y, z-1], xmin, xmax, ymin, ymax, zmin, zmax, input_, steam)
        if z+1 < zmax: fill([x, y, z+1], xmin, xmax, ymin, ymax, zmin, zmax, input_, steam)
        if y-1 > ymin: fill([x, y-1, z], xmin, xmax, ymin, ymax, zmin, zmax, input_, steam)
        if y+1 < ymax: fill([x, y+1, z], xmin, xmax, ymin, ymax, zmin, zmax, input_, steam)
        if x-1 > xmin: fill([x-1, y, z], xmin, xmax, ymin, ymax, zmin, zmax, input_, steam)
        if x+1 < xmax: fill([x+1, y, z], xmin, xmax, ymin, ymax, zmin, zmax, input_, steam)
    return
    