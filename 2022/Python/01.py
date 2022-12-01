def generator(file) :
    return [[int(calories) for calories in reeinder.splitlines()] for reeinder in file.split("\n\n")]

def part_1(input) : 
    return max([sum(reeinder) for reeinder in input])

def part_2(input) : 
    return sum(sorted([sum(item) for item in input])[-3:])