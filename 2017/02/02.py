import re
from itertools import product

def generator(input):
    return [[int(item) for item in re.findall('[0-9]+',line)] for line in input.splitlines()]

def part_1(input):
    return sum([max(s) - min(s) for s in input])

def part_2(input):
    return sum([a // b for (a, b) in product(line, repeat = 2) if a % b == (a == b)][0] for line in input)
            
