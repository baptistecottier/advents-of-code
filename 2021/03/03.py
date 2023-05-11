def generator(input): 
    diagnostic = input.splitlines()
    return (len(diagnostic[0]), len(diagnostic),  [int(item, base = 2) for item in diagnostic])

def part_1(input):
    gamma_rate = sum(2 ** k * most_common_bit(input, k) for k in range(input[0]))
    return (2 ** input[0] - 1 - gamma_rate) * gamma_rate

def part_2(input): 
    w, _, data = input
    ratings = 1
    for b in range(2):
        diag, k = data, w
        while len(diag) > 1:
            bit = most_common_bit((w, len(diag), diag), k := k - 1) ^ b
            diag = [item for item in diag if (item >> k) & 1 == bit]
        ratings *= diag.pop()
    return ratings

def most_common_bit(input, n):
    return sum(((a >> n) & 1) for a in input[2]) >= input[1] / 2


    