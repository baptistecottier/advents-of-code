def generator(input): 
    details = []
    ways = [(1,0) , (0, -1), (-1, 0), (0,1)]
    dir = 0
    
    for step in input.split(', '):
        dir = (dir  - 1 + 2 * (step[0] == 'R')) % 4
        details.append((ways[dir],int(step[1:])))
    
    return details


def part_1(input):
    x, y = solver(input)[-1]
    return abs(x) + abs(y)


def part_2(input): 
    path = solver(input)
    visited = []
    for x, y in path: 
        if (x, y) in visited : return abs(x) + abs(y)
        else : visited.append((x,y))


def solver(input):
    x, y = 0 , 0
    path = [(x,y)]
    for (dx, dy) , steps in input: 
        for _ in range(1,steps + 1):
            x += dx
            y += dy
            path.append((x, y))
    
    return path
        