import itertools
from math import prod
def preprocessing(input):
    return [int(expense) for expense in input.splitlines()]

def solver(input):
    yield find_entries(input, 2)
    yield find_entries(input, 3)
        
def find_entries(input, n):
    for c in itertools.product(input, repeat = n):
        if sum(c) == 2020: 
            return prod(c)
