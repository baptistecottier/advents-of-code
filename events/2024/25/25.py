from itertools import product

def preprocessing(puzzle_input):
    keys = list()
    locks = list()
    
    blocks = puzzle_input.split('\n\n')
    for raw_block in blocks:
        raw_block = raw_block.replace('\n', '')
        block = [-1, -1, -1, -1, -1]
        for i, c in enumerate(raw_block):
            if c == '#':
                block[i % 5] += 1
        if raw_block.startswith("#####"):
            if block not in locks:
                locks.append(block)
        elif block not in keys: 
                keys.append(block)
    return locks, keys
                

def solver(locks, keys):
    pairs = 0
    for l, k in product(locks, keys):
        if all((ll + kk) <= 5 for ll, kk in zip(l, k)):
            pairs += 1
    yield pairs