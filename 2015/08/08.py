def generator(input): 
    return input.splitlines()

def part_1(strings): 
    return sum(len(string) - len(eval(string)) for string in strings)

def part_2(strings): 
    return sum(2 + string.count('\"') + string.count('\\') for string in strings)