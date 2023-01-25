from math import log

def generator(input): return int(input)

def part_1(input): return solver(input, 2)

def part_2(input): return solver(input, 3)

def solver(input, n):
    logn = int(log(input, n))
    winner = input % (n ** logn)
    if n-1 < input / (n ** logn) < n : winner += n ** ((n-2) * logn) + winner
    return winner