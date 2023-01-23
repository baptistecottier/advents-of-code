import re

def generator(input): 
    return [int(item) for item in re.findall('[0-9]+', input)]


def part_1(input): 
    return solver(input, 1)


def part_2(input):
    return solver(input, 3)


def solver(input, v):
    valid = 0
    for t in range(len(input) // 3):
        first_elem = t % v + (t // v) * (3 * v)
        sides = input[first_elem : first_elem + 1 + 2 * v][::v]
        sides.sort()
        valid += (sides[0] + sides[1] > sides[2]) 
        
    return valid