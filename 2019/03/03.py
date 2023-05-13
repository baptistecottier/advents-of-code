def generator(input): 
    return [[[dir_match(item[0]), int(item[1:])] for item in wire.split(',')] for wire in input.splitlines()]
    
def part_1(input):
    return min(solver(input), key = lambda x : x[0])[0]

def part_2(input):
    return min(solver(input), key = lambda x : x[1])[1]


def dir_match(dir):
    match dir :
        case 'R': return (1, 0)
        case 'L': return (-1, 0)
        case 'U': return (0, 1)
        case 'D': return (0, -1)
        
def solver(input):
    wires, crossed = {}, set()
    x, y, steps = 0, 0, 0
    for [(dx, dy), n] in input[0]:
        for i in range(1, n + 1): 
            wires[(x + i * dx, y + i * dy)] = steps + i
        x, y, steps = x + n * dx, y + n * dy, steps + n

    x, y, steps = 0, 0, 0
    for [(dx, dy), n] in input[1]:
        for i in range(1, n + 1): 
            xx, yy = x + i * dx, y + i * dy
            if (xx, yy) in wires: 
                manhattan = abs(xx) + abs(yy)
                step =  steps + i + wires[(xx, yy)]
                crossed.add((manhattan, step))
        x, y, steps = x + n * dx, y + n * dy, steps + n

    return crossed