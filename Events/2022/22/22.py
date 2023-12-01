import re

def preprocessing(input_):
    data = []
    bm, path = input_.split('\n\n')
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
            
        

def part_2(input_): 
    dx, dy = 1, 0
    data, steps, turns = input_
    for step in steps: 
        infos = data[y]
        modulo = infos[1] - infos[0]
        if dy == 0: 
            if dx == 1: x = min((x + step) % modulo , min([n for n in infos[2] if n > x]))
            if dx == -1: x = max((x - step) % modulo , min([n for n in infos[2] if n > x]))
        
    
    
    
    
    return 2

def part_1(input_): return input_