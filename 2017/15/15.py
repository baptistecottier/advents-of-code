def generator(input):
    return [int(line.rsplit(' ',1)[-1]) for line in input.splitlines()]

def part_1(input): 
    return solver(input, False)

def part_2(input): 
    return solver(input, True)

def solver(input, picky_generators): 
    a, b = input
    cnt = 0 
    if picky_generators : (rounds, mult_a, mult_b) = (5_000_000, 4, 8)
    else : (rounds, mult_a, mult_b) = (40_000_000, 1, 1)
    for i in range(rounds):
        a = (a * 16807) % 2147483647
        while a % mult_a != 0 : a = (a * 16807) % 2147483647

        b = (b * 48271) % 2147483647
        while b % mult_b != 0 : b = (b * 48271) % 2147483647
        
        if a % (2 ** 16) == b % (2 ** 16): cnt += 1
    return cnt

