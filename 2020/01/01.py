import itertools
from math import prod
def generator(input) :
    return [int(expense) for expense in input.splitlines()]

def part_1(input) :
    return solver(input, 2)

def part_2(input) : 
    return solver(input, 3)
        
def solver(input, n):
    for c in list(itertools.product(input, repeat = n)):
        if sum(c) == 2020 : 
            return prod(c)
