def parser(data): 
    directions = list(1 if direction == '(' else -1 for direction in data)
    return directions

def solver(directions):
    floor  = 0
    length = len(directions)
    
    yield sum(directions)
    
    while directions: 
        floor += directions.pop(0)
        if floor < 0: 
            yield length - len(directions)
            return