def generator(input) : 
    paths = []
    for line in input.splitlines() : 
        rock_path = []
        for pos in line.split(' -> ') :
            rock_path.append([int(item) for item in pos.split(',')])
        paths.append(rock_path)
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    max_depth = 0
    for path in paths : 
        for i in range(len(path) -1):
            [xa, ya] , [xb, yb] = path[i] , path[i+1]
            for y in range(min(ya, yb), max(ya, yb)+1):
                max_depth = max(y, max_depth)
                for x in range(min(xa, xb), max(xa, xb)+1):
                    grid[y][x] = 1
    return grid, max_depth

def part_1(input) : 
    return solver(input, False)

def part_2(input) : 
    return solver(input, True)
            

def solver(input, floor) :
    grid, max_depth = input
    if floor : 
        max_depth += 2
        for x in range(1000) : grid[max_depth][x] = 1

    cnt = 0
    x, y = 500, 0
    while True :
        if grid[0][500] == 1 or y >= max_depth : return cnt
        if grid[y+1][x] == 0 : y += 1
        elif all([grid[y+1][i] == 1 for i in [x-1, x + 1]]) :
            grid[y][x] = 1
            cnt += 1
            x, y = 500, 0
        elif grid[y+1][x-1] == 0 : x , y = x - 1 , y + 1
        elif grid[y+1][x+1] == 0 : x, y = x + 1, y + 1
