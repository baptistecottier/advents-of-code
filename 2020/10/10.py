from math import prod

def generator(input):
    joltages = sorted(int(item) for item in sorted(input.splitlines()))
    return [0] + joltages + [joltages[-1] + 3]

def part_1(input):
    differences = [b - a for a, b in zip(input[:-1], input[1:])]
    return differences.count(3) *  differences.count(1)

def part_2(input): 
    differences = [b - a for a, b in zip(input[:-1], input[1:])]
    groups = []
    while differences:
        cnt = 0
        while differences and differences.pop() == 1: cnt += 1
        if cnt > 1: groups.append(cnt)
    return prod([2 ** (v - 1) - (v == 4) for v in groups])
