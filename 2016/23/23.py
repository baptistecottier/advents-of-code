from math import factorial

def generator(input): 
    return [line.split(' ', 1) for line in input.splitlines()]

def part_1(input) : 
    return solver(input, 7)

def part_2(input) : 
    return solver(input, 12)

def solver(input, a) : 
    return factorial(a)  + int(input[19][1][:-2]) * int(input[20][1][:-2])