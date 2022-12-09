def generator(input) :
    return [sorted([int(size) for size in present.split('x')]) for present in input.splitlines()]

def part_1(dimensions) :
    return sum([2 * h * (l + w) + 3 * l * w for [l,w,h] in dimensions])

def part_2(dimensions) : 
    return sum([2 * (l + w) + l * w * h for [l,w,h] in dimensions])
