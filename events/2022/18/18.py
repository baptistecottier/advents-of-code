def preprocessing(puzzle_input): 
    grid = []
    for line in puzzle_input.splitlines(): 
        grid.append([int(item) for item in line.split(',')])
    
    return grid 

import itertools 

def solver(puzzle_input): 
    cnt = 0
    for i, a in enumerate(puzzle_input): 
        for j, b in enumerate(puzzle_input[i+1:]):
            if  any(a[n % 3] == b[n % 3] \
                    and a[(n + 1) % 3] == b[(n + 1) % 3]\
                    and abs(a[(n + 2) % 3] - b[(n + 2) % 3]) == 1 \
                for n in range(3)): cnt += 1
        
    yield 6 * len(puzzle_input) - 2 * cnt

def part_2(puzzle_input): 
    max_x = max([a[0] for a in puzzle_input])
    max_y = max([a[1] for a in puzzle_input])
    max_z = max([a[2] for a in puzzle_input])
    min_x = min([a[0] for a in puzzle_input])
    min_y = min([a[1] for a in puzzle_input])
    min_z = min([a[2] for a in puzzle_input])
    steam = []
    air = []
    fill([0,0,0], min_x, max_x, min_y, max_y, min_z, max_z, puzzle_input, steam)
    for x in range(min_x, max_x): 
        for y in range(min_y, max_y): 
            for z in range(min_z, max_z): 
                if [x, y, z] not in steam and [x, y, z] not in puzzle_input: air.append([x,y,z])
    print("air:", air)

def fill(pos, xmin, xmax, ymin, ymax, zmin, zmax, puzzle_input, steam):
    steam.append(pos)
    print(pos)
    if pos in puzzle_input or pos in steam: 
        return
    else: 
        [x, y, z] = pos
        if z-1 > zmin: fill([x, y, z-1], xmin, xmax, ymin, ymax, zmin, zmax, puzzle_input, steam)
        if z+1 < zmax: fill([x, y, z+1], xmin, xmax, ymin, ymax, zmin, zmax, puzzle_input, steam)
        if y-1 > ymin: fill([x, y-1, z], xmin, xmax, ymin, ymax, zmin, zmax, puzzle_input, steam)
        if y+1 < ymax: fill([x, y+1, z], xmin, xmax, ymin, ymax, zmin, zmax, puzzle_input, steam)
        if x-1 > xmin: fill([x-1, y, z], xmin, xmax, ymin, ymax, zmin, zmax, puzzle_input, steam)
        if x+1 < xmax: fill([x+1, y, z], xmin, xmax, ymin, ymax, zmin, zmax, puzzle_input, steam)
    return
    