from itertools import product

def generator(input):
    return [[int(item) for item in line.split(', ')] for line in input.splitlines()]

def part_1(input):
    grid = [[0 for _ in range(500)] for _ in range(500)]
    for x, y in product(range(500), range(500)):
        distances = []
        for n, (xx, yy) in enumerate(input):
            distances.append([n,abs(xx-x)+abs(yy-y)])
        distances = [item for item in distances if item[1] == min([d[1] for d in distances])]
        if len(distances) == 1: grid[y][x] = distances[0][0]
        else : grid[y][x] = -1
    infinites = []
    infinites += [grid[0][x] for x in range(500)]
    infinites += [grid[-1][x] for x in range(500)]
    infinites += [grid[y][0] for y in range(500)]
    infinites += [grid[y][-1] for y in range(500)]
    infinites = list(set(infinites))
    
    max_count = 0
    for n in [item for item in range(len(input)) if item not in infinites]:
        print(n)
        count = sum([grid[y][x] == n for x, y in product(range(500), range(500))])
        max_count = max(max_count, count)
    return max_count        

def part_2(input):
    cnt = 0
    for x, y in product(range(500), range(500)):
        distances = []
        for xx, yy in input:
            distances.append(abs(xx-x)+abs(yy-y))
        if sum(distances) < 10_000 : cnt += 1
    return cnt