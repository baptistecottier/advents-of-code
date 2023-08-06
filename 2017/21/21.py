from itertools import product

def preprocessing(input_):
    rules = {}
    for line in input_.splitlines():
        pattern, replacement = line.replace('/','').split(' => ')
        r1, r2, r3 = rotate(pattern, 1),  rotate(pattern, 2),  rotate(pattern, 3)
        f, f1, f2, f3 = flip(pattern), flip(r1), flip(r2) , flip(r3)
        for p in [pattern, r1, r2, r3, f, f1, f2, f3]:
            rules[p]=replacement
    return rules

def flip(input_):
    size = int(len(input_) ** 0.5)
    return ''.join([''.join(input_[i * (size): i * size + size])[::-1] for i in range(size)]) 

def rotate(input_, n):
    perm = [[2,0,3,1], [6,3,0,7,4,1,8,5,2]]
    for _ in range(n):
        size = int(len(input_) ** 0.5) - 2
        input_ =''.join([input_[perm[size][i]] for i in range(len(input_))])
    return input_

def solver(input_):
    grid = '.#...####'
    for m in range(18):
        size = int(len(grid) ** 0.5)
        if size % 2 == 0: divisor = 2 
        else: divisor = 3
        enhanced_grid = []
        for r, c in product(range(size // divisor), range(size // divisor)):
            index = (r * size + c) * divisor
            mini_grid = ''.join([grid[index + i * size: index + i * size + (divisor)] for i in range(divisor)])
            enhanced_grid.append(input_[mini_grid])
        grid = ''
        for i in range(size + size // divisor):
            ii = (i * (divisor + 1)) % (divisor + 1) ** 2
            jj = (i // (divisor + 1)) * (size // divisor) 
            for j in range(size // divisor):
                grid += enhanced_grid[jj + j][ii: ii + (divisor + 1)]
        if m == 4: yield grid.count('#')
    yield grid.count('#')