def generator(input):
    return list(map(lambda x: (x[0], int(x[1:])), input.splitlines()))

def part_1(input):
    return solver(input, False, 1, 0)

def part_2(input): 
    return solver(input, True, 10, 1)

def solver(input, waypoint, dx, dy): 
    x, y = 0, 0
    for act, val in input:
        tx, ty = 0, 0
        match act:
            case 'N': ty = val
            case 'S': ty = -val
            case 'E': tx = val
            case 'W': tx = -val
            case 'L': dx, dy = [dx, -dy, -dx, dy][val // 90], [dy, dx, -dy, -dx][val // 90]
            case 'R': dx, dy = [dx, dy, -dx, -dy][val // 90], [dy, -dx, -dy, dx][val // 90]
            case 'F': x, y = x + val * dx, y + val * dy
        if waypoint: dx, dy = dx + tx, dy + ty
        else: x, y = x + tx, y + ty
    return abs(x) + abs(y)