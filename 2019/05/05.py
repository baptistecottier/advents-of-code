import ship_computer
from copy import deepcopy

def generator(input): 
    return ship_computer.generator(input)

def part_1(input):
    return ship_computer.run(input, [1]).pop()

def part_2(input): 
    return ship_computer.run(input, [5]).pop()
