from itertools import pairwise
from collections import Counter
from operator import eq, ge

def generator(input): return [int(item) for item in input.split('-')]

def part_1(input): return solver(input, ge)

def part_2(input): return solver(input, eq)


def solver(input, op):
    return sum([not any([a > b for (a, b) in pairwise(str(pw))]) and any( op(n,2) for (_, n) in Counter(str(pw)).most_common()) for pw in range(input[0], input[1] + 1)])