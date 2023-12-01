from itertools import combinations
from re        import findall

def preprocessing(input):
    details = []
    for data in input.split('mask = ')[1:]:
        data       = data.splitlines()
        not_masked = [i for i in range(36) if data[0][::-1][i] == 'X']
        mask       = int(data[0].replace('X','0'), base = 2)
        mem        =  [map(int, findall(r'[0-9]+', d)) for d in data[1:]]
        details.append([mask, not_masked, mem])
    return details

def solver(input): 
    memory = {1: dict(), 2: dict()}
    for mask, not_masked, mem in input:
        for adr, val in mem:
            memory[1][adr] = mask + sum([(val >> n & 1) * (2 ** n) for n in not_masked])
            result = mask | adr
            for b in not_masked: result &=~ (1 << b)
            for l in range(0, 1 + len(not_masked)):
                for bits in combinations(not_masked, l):
                    memory[2][result + sum([(2 ** n) for n in list(bits)])] = val
    yield sum(memory[1].values())
    yield sum(memory[2].values())