from pythonfw.classes import Point

def preprocessing(input):
    return list(map(lambda x: (x[0], int(x[1:])), input.splitlines()))

def solver(instructions):
    yield navigate(instructions, False, 1, 0)
    yield navigate(instructions, True, 10, 1)

def navigate(instructions, waypoint, dx, dy): 
    pos = Point()
    for act, val in instructions:
        tx, ty = 0, 0
        match act:
            case 'N': ty = val
            case 'S': ty = -val
            case 'E': tx = val
            case 'W': tx = -val
            case 'L': dx, dy = [(dx, dy), (-dy, dx), (-dx, -dy), (dy, -dx)][val // 90]
            case 'R': dx, dy = [(dx, dy), (dy, -dx), (-dx, -dy), (-dy, dx)][val // 90]
            case 'F': pos.move(val * dx, val * dy)
        if waypoint: dx, dy = dx + tx, dy + ty
        else: pos.move(tx, ty)
    return pos.manhattan()