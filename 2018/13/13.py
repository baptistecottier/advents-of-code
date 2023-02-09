def generator(input):
    grid = [list(r) for r in input.splitlines()]
    carts = []
    for r, l in enumerate(grid):
        for c, p in enumerate(l):
            if p in ['>', 'v', '<', '^']: carts.insert(0, ((c, r), ((p == '>') - (p == '<'), (p == 'v') - (p == '^')), 0))
    return (grid, carts)

def part_1(input): 
    crash = solver(input, len(input[1]) - 2)
    return ','.join([str(item) for item in crash[1]])
    
def part_2(input): 
    crash = solver(input, 1)
    return ','.join([str(item) for item in crash[0][0][0]])
        
        
def solver(input, trigger): 
    grid, carts = input
    s = 0
    while len(carts) != trigger: 
        ((x, y), (dx, dy), choice) = carts.pop()
        x, y = x + dx, y + dy
        if (x,y) in [item[0] for item in carts]: 
            carts = [item for item in carts if item[0] != (x, y)]
            continue
        match (grid[y][x], abs(dx)):
            case ('+', _): carts.insert(0,((x,y), turn((dx, dy), choice), (choice + 1) % 3 ))
            case ('/', 1): carts.insert(0,((x,y), turn_left((dx, dy)), choice ))
            case ('/', 0): carts.insert(0,((x,y), turn_right((dx, dy)), choice ))
            case ('\\', 1): carts.insert(0,((x,y), turn_right((dx, dy)), choice ))
            case ('\\', 0): carts.insert(0,((x,y), turn_left((dx, dy)), choice ))
            case _ : carts.insert(0, ((x, y), (dx, dy), choice))
        s += 1
        if s % len(carts) == 0 : carts.sort(key = lambda x: (-x[0][0], -x[0][1]))
    return (carts, (x, y))
    
def turn(dir, choice):
    match choice: 
        case 0: return turn_left(dir)
        case 1: return dir
        case 2: return turn_right(dir)
    
    
def turn_right(dir):
    match dir: 
        case (n, 0): return (0, n)
        case (0, n): return (-n, 0)


def turn_left(dir):
    match dir: 
        case (n, 0): return (0, -n)
        case (0, n): return (n, 0)