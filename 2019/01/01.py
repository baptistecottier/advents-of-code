def generator(input):
    return [int(item) for item in input.splitlines()]
    
def part_1(input):
    return sum(compute_fuel(input))

def part_2(input):
    acc = 0 
    while input:
        input = compute_fuel(input)
        acc += sum(input)
    return acc


def compute_fuel(input):
    return [item // 3 - 2 for item in input if item > 5]