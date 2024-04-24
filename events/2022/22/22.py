import re

def preprocessing(puzzle_input):
    data = []
    bm, path = puzzle_input.split('\n\n')
    for row in bm.splitlines():
        min_x = row.count(' ')
        max_x = len(row) - 1
        walls = []
        for n in range(min_x, max_x + 1):
            if row[n] == '#': walls.append(n)
        data.append([min_x, max_x, walls])
        
    steps = [int(item) for item in re.findall(r'\d+', path)]
    turns = re.findall(r'[LR]', path)
    return data, steps, turns
            
        

def part_2(puzzle_input): 
    dx, dy = 1, 0
    data, steps, turns = puzzle_input
    for step in steps: 
        infos = data[y]
        modulo = infos[1] - infos[0]
        if dy == 0: 
            if dx == 1: x = min((x + step) % modulo , min([n for n in infos[2] if n > x]))
            if dx == -1: x = max((x - step) % modulo , min([n for n in infos[2] if n > x]))
        
    
    
    
    
    return 2

def part_1(puzzle_input): return puzzle_input