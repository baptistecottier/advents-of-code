from parse import parse
from itertools import combinations

def generator(input):
    details = []
    for data in input.split('mask = ')[1:]:
        data = data.splitlines()
        not_masked = [i for i in range(36) if data[0][::-1][i] == 'X']
        mask = int(data[0].replace('X','0'), base = 2)
        mem = [parse("mem[{:d}] = {:d}", d)[:2] for d in data[1:]]
        details.append([mask, not_masked, mem])
    return details

def part_1(input): 
    memory = {}
    for mask, not_masked, mem in input:
        for adr, val in mem:
            memory[adr] = mask + sum([(val >> n & 1) * (2 ** n) for n in not_masked])
    return sum(memory.values())
        
def part_2(input): 
    memory = {}
    for mask, not_masked, mem in input:
        for adr, val in mem:
            result = mask | adr
            for b in not_masked: result &=~ (1 << b)
            for l in range(0, 1 + len(not_masked)):
                for bits in combinations(not_masked, l):
                    memory[result + sum([(2 ** n) for n in list(bits)])] = val
    return sum(memory.values())