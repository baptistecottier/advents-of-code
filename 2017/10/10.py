from AoC_tools import knot_hash

def generator(input):
    return input

def part_1(input):
    pos, size = 0, 256
    numbers = list(range(size))
    for (skip, l) in enumerate([int(item) for item in input.split(',')]) :
        temp=numbers.copy()
        for i in range(l):
            numbers[(pos+i)%size]=temp[(pos+l-i-1) % size]
        pos=(pos+l+skip) % size
    return numbers[0]*numbers[1]

def part_2(input):
    return knot_hash(input, 256)