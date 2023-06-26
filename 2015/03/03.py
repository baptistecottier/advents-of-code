from copy import deepcopy


from copy import deepcopy

def parser(data):
    converter = {'^': (0, 1), '>': (1, 0), 'v': (0, -1), '<': (-1, 0)}
    directions = list(converter.get(d) for d in data)
    return directions

def solver(DIRECTIONS):
    def deliver(n):
        directions = deepcopy(DIRECTIONS)
        deliverers = [(0, 0) for _ in range(n)]
        houses     = {(0, 0)}
        
        while directions:
            for k in range(n):
                dx, dy = directions.pop(0)
                x, y   = deliverers.pop(0)
                x, y   = x + dx, y + dy
                houses.add((x, y))
                deliverers.append((x, y))
        return len(houses)
    
    yield deliver(1)
    yield deliver(2)