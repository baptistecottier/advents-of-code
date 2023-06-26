from math import factorial

def parser(input): 
    return list(line.split(' ', 1) for line in input.splitlines())

def solver(instructions):
    delta = int(instructions[19][1][:-2]) * int(instructions[20][1][:-2])
    yield factorial(7)  + delta
    yield factorial(12) + delta