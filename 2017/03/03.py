from itertools import product

def generator(input): return int(input)

def part_1(input):
    return int(((input - 1) ** 0.5 + 1) // 2) + (input + int(((input - 1) ** 0.5 + 1) // 2) - 1) % int(((input - 1) ** 0.5 + 1) // 2)

def part_2(input): 
    memory=[[0 for _ in range(20)] for _ in range(20)]
    x, y = 10, 10
    next_directions={(1,0):(0,1), (0,1):(-1,0), (-1,0):(0,-1), (0,-1):(1,0)}
    vx, vy = 0, -1
    tx, ty = next_directions[(vx,vy)]
    value = 1
    memory[y][x] = value
    while value <= input:
        if memory[y + ty][x + tx] == 0:
            x, y = x + tx, y + ty
            vx, vy = tx, ty
            tx, ty = next_directions[(tx, ty)]
        else: x, y = x + vx, y + vy
        value=sum(memory[dy][dx] for (dx,dy) in product([x-1, x, x+1], [y-1, y, y+1]))
        memory[y][x]=value
    return value
