from pythonfw.classes import Point

def preprocessing(data: str): 
    ways = [(1,0) , (0, -1), (-1, 0), (0,1)]
    dir  = 0
    path = list()
    
    for step in data.split(', '):
        match step[0]:
            case 'L': dir = (dir - 1) % 4
            case 'R': dir = (dir + 1) % 4
        path.append((ways[dir], int(step[1:])))
        
    return path

def solver(path):
    pos     = Point()
    visited = {pos.xy()}
    twice   = False
    
    while path:
        (dx, dy), steps = path.pop(0)
        for _ in range(steps):
            pos.move(dx, dy)
            if not twice:
                if pos.xy() in visited:
                    yield (2, pos.manhattan())
                    twice = True
                else: visited.add(pos.xy())
    yield (1, pos.manhattan())