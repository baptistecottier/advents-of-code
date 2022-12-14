def generator(input) : 
    paths = []
    cave = [[0 for _ in range(1000)] for _ in range(200)]
    for line in input.splitlines() : 
        rock_path = []
        for pos in line.split(' -> ') :
            rock_path.append([int(item) for item in pos.split(',')])
        paths.append(rock_path)

    max_depth = 0
    for path in paths : 
        for [xa, ya] , [xb, yb] in zip(path, path[1:]):
            for x, y in range(min(ya, yb), max(ya, yb)+1):
                max_depth = max(y, max_depth)
                for x in range(min(xa, xb), max(xa, xb)+1):
                    cave[y][x] = 1
                    
    for x in range(1000) : cave[max_depth + 2][x] = 1

    return cave, max_depth

def part_1(input) : 
    return solver(input[0], input[1], False)

def part_2(input) : 
    return solver(input[0], input[1], True)
            

def solver(cave, max_depth, floor) :
    x, y, sand = 500, 0, 0
    
    while cave[0][500] == 0 and y < max_depth + 2 * floor :
        match (cave[y+1][x-1] , cave[y+1][x] , cave[y+1][x+1]) :
            case (_, 0, _ )  : y += 1
            case (0, _, _)   : (x , y) = (x - 1, y + 1)
            case (_, _, 0)   : (x , y) = (x + 1, y + 1)
            case _           : 
                cave[y][x] = 1
                (x, y) = (500, 0)
                sand += 1

    return sand
