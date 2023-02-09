from itertools import product

def generator(input): 
    return input.splitlines()

def part_1(input):
    twice = 0
    thrice = 0
    for id in input: 
        counts = [id.count(c) for c in id]
        twice += 2 in counts
        thrice += 3 in counts
    return twice * thrice        
        
def part_2(input):
    for ida, idb in product(input, input):
        if sum([ida[i] != idb[i] for i in range(len(ida))]) == 1 : 
            return ''.join([item for item in ida if item in idb])
        