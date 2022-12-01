def generator(file) :
    return [[int(x) for x in item.split("\n")] for item in file.split("\n\n")]

def part_1(input) : 
    return max([sum(x) for x in input])

def part_2(input) : 
    return sum(sorted([sum(item) for item in input])[-3:])