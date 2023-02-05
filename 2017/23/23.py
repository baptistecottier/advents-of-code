def generator(input):
    return [int(item) for item in [line.split(' ')[-1] for line in input.splitlines() if not line.split(' ')[-1].isalpha()]]
            
def part_1(input):
    p = input[0] - input[7]
    q = input[0] - input[8]
    return p * q

def part_2(input): 
    h = 0
    b = input[0] * input[3] - input[4]
    c = b - input[5]
    step = - input[-2]
    for i in range(b, c + 1, step):
        d = input[7]
        while i % d != 0: d += 1
        if i != d: h += 1
    return h