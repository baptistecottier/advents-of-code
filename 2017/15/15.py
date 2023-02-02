def generator(input):
    return [int(line.rsplit(' ',1)[-1]) for line in input.splitlines()]

def part_1(input): 
    return solver(input, 40_000_000, 1, 1)

def part_2(input): 
    return solver(input, 5_000_000, 4, 8)

def solver(input, rounds, mult_a, mult_b): 
    a, b = input
    matching_pairs = 0 
    for i in range(rounds):
        a = (a * 16807) % 2147483647
        while a % mult_a != 0 : a = (a * 16807) % 2147483647

        b = (b * 48271) % 2147483647
        while b % mult_b != 0 : b = (b * 48271) % 2147483647
        
        if a % (2 ** 16) == b % (2 ** 16): matching_pairs += 1
    return matching_pairs

