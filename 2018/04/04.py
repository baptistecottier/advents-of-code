from parse import parse
from itertools import pairwise, product

def generator(input):
    records = []
    for line in input.splitlines():
        records.append(parse("[{:d}-{:d}-{:d} {:d}:{:d}]{}", line)[:6])
    records.sort()
    return records
    
def part_1(input): 
    asleep = solver(input)
    max_asleep = max(asleep.keys(), key = lambda x: sum(asleep[x]))
    return max_asleep  * max(range(60), key = lambda i: asleep[max_asleep][i])
    
def part_2(input):
    asleep = solver(input)
    guard, min = max(product(asleep.keys(), range(60)), key = lambda g: asleep[g[0]][g[1]])
    return guard * min
    
    
def solver(input):
    asleep = {}
    for a, b in pairwise(input):
        if 'Guard' in a[-1]:
            guard = get_guard_id(a[-1])
            if guard not in asleep : asleep[guard] = [0 for _ in range(60)]
        elif 'Guard' in b[-1]:
            guard = get_guard_id(b[-1])
            if guard not in asleep : asleep[guard] = [0 for _ in range(60)]
        elif 'asleep' in a[-1]:
            for i in range(a[-2], b[-2]): asleep[guard][i] += 1
    
    return asleep
        
def get_guard_id(infos):
    return int(infos.split(' ')[2][1:])