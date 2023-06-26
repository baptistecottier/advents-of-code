from itertools import groupby

def parser(input): 
    return input 

def solver(digits):
    yield conway(digits, 40)
    yield conway(digits, 50)

def conway(digits, cycles):    
    for _ in range(cycles):
        digits = "".join(f"{len(list(l))}{k}" for k, l in groupby(digits))
    return len(digits)
    