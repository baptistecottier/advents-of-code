from AoC_tools import bfs

def generator(input): 
    return int(input)


def part_1(input): 
    return solver(input, (31, 39))


def part_2(input): 
    values = [solver(input,(x,y)) for x in range(50) for y in range(50-x)]
    return sum([item <= 50 for item in values if item != None])


def solver(input, target):
    maze=[['.' for _ in range(50)] for _ in range(50)]

    for x in range(50):
        v = x * (x + 3) + input
        for y in range(50):
            if bin(v).count('1') % 2 : maze[y][x]='#'
            v += 2 * (x + y + 1)

    return bfs(maze, (1,1) , target)

