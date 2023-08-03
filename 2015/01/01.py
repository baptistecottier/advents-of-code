def parser(input_): 
    directions = list(1 if direction == '(' else -1 for direction in input_)
    return directions


def solver(directions):
    floor    = 0
    basement = False    
    
    for i, dir in enumerate(directions, 1):
        floor += dir
        if not basement and floor < 0: 
            yield (2, i)
            basement = True
    yield (1, floor)