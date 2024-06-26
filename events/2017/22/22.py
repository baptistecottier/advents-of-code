def preprocessing(puzzle_input): 
    infected = []
    grid = puzzle_input.splitlines()
    size = len(grid)
    for y, line in enumerate(grid[::-1]):
        for x, c in enumerate(line):
            if c == '#': infected.append((x, y))
    return infected, size

def solver(infected, size): 
    yield burst(infected, size, 1)
    yield burst(infected, size, 2)


def burst(infected, size, bursts):
    half_grid_size = 400
    grid = [[0 for _ in range(2 * half_grid_size)] for _ in range(2 * half_grid_size)]
    for x, y in infected: grid[half_grid_size - (size // 2) + y][half_grid_size - (size // 2) + x] = bursts
    cx, cy = half_grid_size, half_grid_size
    dx, dy = 0, 1
    cnt = 0
    
    for _ in range(10**(1 + 3 * bursts)):
        grid[cy][cx] = (grid[cy][cx] + 1) % (2 * bursts)
        if grid[cy][cx] == bursts: cnt += 1
        
        if grid[cy][cx] == -3 + 3 * bursts: dx, dy = turn_right((dx, dy))
        elif grid[cy][cx] == 1: dx, dy = turn_left((dx, dy))
        elif grid[cy][cx] == 0: dx, dy = -dx, -dy
        
        cx, cy = cx + dx, cy + dy
    return cnt

def turn_left(dir):
    match dir: 
        case (n, 0): return (0, n)
        case (0, n): return (-n, 0)

def turn_right(dir):
    match dir: 
        case (n, 0): return (0, -n)
        case (0, n): return (n, 0)
        