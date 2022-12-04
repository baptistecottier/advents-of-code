def generator(input) :
    return input.splitlines()

def part_1(input) : 
    return solver(input, 1)

def part_2(input) : 
    return solver(input, 3)

def solver(input, size) : 
    return sum(ord([x for x in input[size * i : size * (i + 1)][0][:- (size % 3) * len(input[size * i : size * (i + 1)][0]) // 2:] if all([x in g[  size % 3 * len(g) //2 :] for g in input[size * i : size * (i + 1)][:size]])][0]) - 38 - [x for x in input[size * i : size * (i + 1)][0][: (size ** 2 % 7) * len(input[size * i : size * (i + 1)][0]) // 2:] if all([x in g[  size % 3 * len(g) //2 :] for g in input[size * i : size * (i + 1)][:size]])][0].islower() * 58 for i in range(len(input) // size))