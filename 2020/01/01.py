from itertools import product
from math      import prod


def preprocessing(input):
    return [int(expense) for expense in input.splitlines()]


def solver(expenses):
    yield find_entries(expenses, 2)
    yield find_entries(expenses, 3)
        

def find_entries(expenses, n):
    for c in product(expenses, repeat = n):
        if sum(c) == 2020: 
            return prod(c)