def generator(input):
    return [passphrase.split(' ') for passphrase in input.splitlines()]

def part_1(input):
    return solver(input, lambda x: x)

def part_2(input):
    return solver(input, sorted)

def solver(input, func):
    return sum([len(["".join(func(p)) for p in pp]) == len(set(["".join(func(p)) for p in pp])) for pp in input])
