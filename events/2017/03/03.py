from collections    import defaultdict
from itertools      import product


def preprocessing(input_): 
    return int(input_)


def solver(square_position):
    circle_index = int(((square_position - 1) ** 0.5 + 1) // 2) 
    yield circle_index + (square_position - 1) % circle_index

    x, y    = 0, 0
    memory  = defaultdict(int)   
    dx, dy  = (0, -1)
    value   = 1
    turn    = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}

    while value < square_position:
        tx, ty = turn[(dx, dy)]
        memory[(x, y)] = value
        if not memory[(x + tx, y + ty)]: dx, dy = tx, ty
        x, y = x + dx, y + dy
        value = sum(memory[(x + tx, y + ty)] for (tx, ty) in product({-1, 0, 1}, repeat = 2))
    yield value
