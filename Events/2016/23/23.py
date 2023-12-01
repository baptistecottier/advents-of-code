from math import factorial

def preprocessing(input_): 
    return list(line.split(' ', 1) for line in input_.splitlines())

def solver(instructions):
    delta = int(instructions[19][1][:-2]) * int(instructions[20][1][:-2])
    yield factorial(7)  + delta
    yield factorial(12) + delta