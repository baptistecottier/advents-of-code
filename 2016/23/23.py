from math import factorial

def generator(input): 
    return list(line.split(' ', 1) for line in input.splitlines())

def part_1(instructions): 
    return run(instructions, 7)

def part_2(instructions): 
    return run(instructions, 12)

def run(instructions, eggs): 
    return factorial(eggs)  + int(instructions[19][1][:-2]) * int(instructions[20][1][:-2])