from parse import parse

def generator(input):
    details = []
    for light in input.splitlines():
        x, y, vx, vy = parse("position=<{:d}, {:d}> velocity=<{:d}, {:d}>", light)[:4]
        details.append(((x, y),(vx, vy)))
    return details

def part_1(input): return solver(input)[1]

def part_2(input): return solver(input)[0]

def solver(input):
    k = 0
    while 1:
        grid = [[' ' for _ in range(501)] for _ in range(501)]
        for ((x,y),(vx, vy)) in input:
            collision = 0
            if 0 <= 250 + y + k * vy <= 500 and 0 <= 250 + x + k * vx <= 500:
                if grid[250 + y + k * vy][250 + x + k * vx] == '#' :
                    collision += 1
                else: grid[250 + y + k * vy][250 + x + k * vx] = '#'
            else: 
                break
        if collision > 0 :
            for x in range(501):
                if any(grid[y][x] == '#' for y in range(501)) : 
                    left = x
                    break            
            for x in range(left, 501)[::-1]:
                if any(grid[y][x] == '#' for y in range(501)) : 
                    right = x+1
                    break
            return (k, '\n'.join([''.join(g[left:right]) for g in grid if '#' in g]))
        k+=1
        
        