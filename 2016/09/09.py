from parse import parse

def generator(input): return input

def part_1(input) : return solver(input, len)

def part_2(input) : return solver(input, part_2)

def solver(s, func):
    for i, c in enumerate(s):
        if c == '(':
            width, rep, _ = parse('({:d}x{:d}){}',s[i:]) 
            length = i + len(str(width)+str(rep)) + 3
            return i + solver(s[length + width:], func) + rep * func(s[length : length + width])
    return len(s)

