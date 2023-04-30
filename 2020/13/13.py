from AoC_tools import chinese_remainder
from math import prod 

def generator(input): 
    details = input.splitlines()
    timestamp = int(details[0])
    bus = [int(item) for item in details[1].replace('x','0').split(',')]
    return timestamp, bus

def part_1(input):
    return prod(min([(-input[0] % id, id) for id in [item for item in input[1] if item != 0]]))

def part_2(input):
    return chinese_remainder(*list(zip(*[(id, -n) for (n, id) in enumerate(input[1]) if id != 0])))