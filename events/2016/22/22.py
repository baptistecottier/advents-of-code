from itertools import product
from pythonfw.functions import extract_chunks
from pythonfw.classes   import Point

class Node():
    def __init__(self, x, y, size, used, avail) -> None:
        self.pt = Point(x, y)
        self.size = size
        self.used = used
        self.avail = avail
        pass
    
def preprocessing(data): 
    return list(Node(*param)for param in extract_chunks(data, take = 5, skip = 1))

def solver(input_):
    yield sum(na.used < nb.avail for (na, nb) in product(input_, input_) if na.used)

    walls = set()
    for node in input_: 
        if node.used == 0: 
            empty = (node.pt)   
        if node.used > 100: 
            walls.add(node.pt)
    pt_min = min(walls, key = lambda x: x.manhattan())
    if pt_min.x != 0: 
        wall = pt_min
        wall.move(-1, 0)
    else: 
        wall = max(walls, key = lambda x: x.manhattan())
        wall.move(1, 0)
    width = max(node.pt.x for node in input_)
    yield empty.manhattan(wall.x, wall.y) + wall.manhattan(width, 0) + 5 * (width - 1)
