from collections import Counter 

def generator(input):
    return [group.split('\n') for group in input.split('\n\n')]

def part_1(input):
    return solver(input, False)

def part_2(input):
    return solver(input, True)

def solver(input, all):
    return sum([len([c for _, c in Counter(''.join(group)).most_common() if c >= all * len(group)]) for group in input])