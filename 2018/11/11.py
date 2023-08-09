from itertools import product

parser = int

def solver(serial): 
    grid      = list(list(x * (x * y + serial) // 100 % 10 - 5 for x in range(11, 311)) for y in range(1, 301))
    width     = 1
    m, x, y   = maximum_power(grid, width)
    max_infos = (x, y, 1)
    max_power = m
    
    while m:
        m, x, y = maximum_power(grid, width := width + 1)
        if width == 3: yield f"{x},{y}"
        if m > max_power: 
            max_power = m
            max_infos = (x, y, width)
    yield ",".join(str(n) for n in max_infos)

def maximum_power(grid, width):
    max_score = 0
    mx, my    = (-1, -1)
    for x, y in product(range(300 - width), repeat = 2):
        score = sum(sum(grid[y + yy][x: x + width]) for yy in range(width))
        if score > max_score: 
            max_score, mx, my = score, x + 1, y + 1
    return max_score, mx, my