def generator(input):
    return [int(item) for item in input.splitlines()]

def part_1(input):
    return solver(input, 1)

def part_2(input): 
    return solver(input, 3)

def solver(input, delta): 
    return sum(input[i+delta] - input[i] > 0 for i in range(len(input) - delta))