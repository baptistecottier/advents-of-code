from pythonfw.classes import Direction

def preprocessing(puzzle_input): 
    directions = list()
    for direction in puzzle_input:
        if direction == '(' : 
            directions.append(Direction(0, 1))
        else :
            directions.append(Direction(0, -1))
    return directions

def solver(directions):
    floor = 0
    steps = 0

    while floor >=0:
        steps += 1
        direc = directions.pop()
        floor += direc.dy
    yield (2, steps)
    while directions:
        direc = directions.pop()
        floor += direc.dy
    yield (1, floor)