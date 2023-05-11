def generator(input): return {n: input.count(str(n)) for n in range(9)}

def part_1(input): return solver(input, 80)

def part_2(input): return solver(input, 256)

def solver(lanternfishes, days):
    for _ in range(days):
        lanternfishes[9] = lanternfishes[0]
        lanternfishes[7] += lanternfishes[0]
        lanternfishes = {x - 1: lanternfishes[x] for x in range(1, 10)}
    return sum(lanternfishes.values())