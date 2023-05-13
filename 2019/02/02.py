
import ship_computer
from itertools import product
from copy import deepcopy

def generator(input):
    return ship_computer.generator(input)

def part_1(input):
    solver(input, 12, 2)
    return input.memory[0]

def part_2(input):
    for (a,b) in product(range(100), repeat = 2):
        program = deepcopy(input)
        solver(program, a, b) 
        if program.memory[0] == 19_690_720 : return 100 * a + b

def solver(program, a, b):
    program.memory[1] = a
    program.memory[2] = b
    return ship_computer.run(program)
    