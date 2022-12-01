import itertools

def generator(input) :
    return [int(expense) for expense in input.splitlines()]

def part_1(input) :
    for (a,b) in list(itertools.product(input, input)):
        if a + b == 2020 : 
            return a * b

def part_2(input) : 
    for (a,b, c) in list(itertools.product(input, input, input)):
        if a + b + c == 2020 : 
            return a * b * c