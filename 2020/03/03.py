from math import prod

def generator(input):
    return [[c == '#' for c in line] for line in input.splitlines()]

def part_1(input): 
    return sum([input[i][(3 * i) % len(input[0])] for i in range(len(input))])

def part_2(input):
    return prod([sum([input[(1 + d // 8) * i][((d % 8) * i) % len(input[0])] for i in range(len(input) // (1 + d // 8))]) for d in range(1,10, 2)])
