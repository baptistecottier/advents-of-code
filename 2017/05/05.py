def generator(input):
    return [int(item) for item in input.splitlines()]
    
def part_1(input):
    return solver(input, 0)

def part_2(input):
    return solver(input, 2)

def solver(jumps, coeff):
    i, steps = 0, 0
    while 0 <= i < len(jumps):
        jumps[i], i = jumps[i] + 1 - coeff * (jumps[i] > 2), i + jumps[i]
        steps += 1
    return steps