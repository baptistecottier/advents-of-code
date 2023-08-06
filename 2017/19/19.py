import enum
from aoctools.classes import Point

def parser(input): 
    path = {}
    for y, row in enumerate(input.splitlines()):
        for x, c in enumerate(row):
            if c != ' ': 
                if y == 0: start = Point(x, y)
                path[(x, y)] = c
    return path, start
    
def solver(map):
    map, pos = map
    dx, dy  = 0, 1
    letters = ""
    steps   = 1

    while 1:
        turn = False
        while (pos.x + dx, pos.y + dy) in map:
            if map[pos.xy()] not in ' |-': letters += map[pos.xy()]
            pos.move(dx, dy)
            steps += 1

        for nx, ny in ((dy, dx), (dy, -dx) if dx else (-dy, dx)):
            if (pos.x + nx, pos.y + ny) in map: 
                dx, dy = nx, ny
                pos.move(dx, dy)
                steps += 1
                turn = True
                break
            
        if not turn: 
            if map.get(pos.xy(), ' ') not in ' |-': letters += map[pos.xy()]
            yield letters
            yield steps
            break        
