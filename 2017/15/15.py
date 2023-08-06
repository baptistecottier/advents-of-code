from itertools import count


def parser(input):
    return [int(line.rsplit(' ')[-1]) for line in input.splitlines()]

def solver(input): 
    yield count_matches(input, 40_000_000, 1, 1)
    yield count_matches(input, 5_000_000, 4, 8)

def count_matches(pair, rounds, mult_a, mult_b): 
    a, b = pair
    matching_pairs = 0 
    for _ in range(rounds):
        a = (a * 16807) % 2147483647
        while a % mult_a != 0: a = (a * 16807) % 2147483647

        b = (b * 48271) % 2147483647
        while b % mult_b != 0: b = (b * 48271) % 2147483647
        
        if  (a - b) % (2 ** 16) == 0 : matching_pairs += 1
    return matching_pairs

