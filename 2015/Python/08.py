def generator(input) : 
    return input.splitlines()

def part_1(input) : 
    return sum([len(line) - len(eval(line)) for line in input])

def part_2(input) : 
    return sum([2+(line.count('\"'))+(line.count('\\')) for line in input])