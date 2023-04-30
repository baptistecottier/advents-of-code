def generator(input):
    return [int(item) for item in input.splitlines()]

def part_1(input):
    p, q = input
    k = 1
    while True:
        key = pow(7, k, 20201227)
        if key == p: return pow(q, k, 20201227)
        if key == q: return pow(p, k, 20201227)
        k += 1

def part_2(input): return "MERRY X-MAS"