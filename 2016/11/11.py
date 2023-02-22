
def generator(input):
    return [floor.count('microchip')+floor.count('generator') for floor in input.splitlines()]

def part_1(input): 
    return solver(input)

def part_2(input):
    input[0] += 4
    return solver(input)


def solver(input): 
    return sum(2*sum(input[:x]) - 3 for x in range(1,4))