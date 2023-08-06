from aoctools.y2017 import knot_hash

def solver(input):
    pos     = 0
    size    = 256
    numbers = list(range(size))
    for skip, l in enumerate(int(item) for item in input.split(',')):
        temp = numbers.copy()
        for i in range(l): numbers[(pos + i) % size] = temp[(pos + l - i - 1) % size]
        pos = (pos + l + skip) % size
    yield numbers[0] * numbers[1]
    yield knot_hash(input, 256)