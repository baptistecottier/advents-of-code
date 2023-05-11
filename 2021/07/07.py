from statistics import mean, median

def generator(input): return [int(item) for item in input.split(',')]

def part_1(input): 
    return solver(input, lambda x: int(median(x)), lambda x : x)

def part_2(input):
    return solver(input, lambda x: int(mean(x)), lambda x: x * (x + 1) // 2)

def solver(crabs, f, g):
    return sum(g(abs(crab - f(crabs))) for crab in crabs)