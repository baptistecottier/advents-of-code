def generator(input: str): 
    x, y : int = 0 , 0
    ways = [(1,0) , (0, -1), (-1, 0), (0,1)]
    path = [(x,y)]
    dir = 0
    for step in input.split(', '):
        match step[0]:
            case 'L': dir = (dir - 1) % 4
            case 'R': dir = (dir + 1) % 4
        dx, dy = ways[dir]
        for step in range(int(step[1:])):
            path.append((x:= x + dx, y:= y + dy))
    return path

def part_1(path):
    x, y = path.pop()
    return abs(x) + abs(y)

def part_2(path): 
    path = path[::-1]
    x, y = path.pop()
    visited = {(x, y)}
    while (point := path.pop()) not in visited: 
        visited.add(point) 
    return abs(point[0]) + abs(point[1])
