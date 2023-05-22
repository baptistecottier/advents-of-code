from itertools import groupby

def generator(input): 
    return input 

def part_1(digits):
    return conway(digits, 40)

def part_2(digits):
    return conway(digits, 50)

def conway(digits, cycles):    
    for _ in range(cycles):
        digits = "".join(f"{len(list(l))}{k}" for k, l in groupby(digits))
    return len(digits)
    