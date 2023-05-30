from parse import parse

def generator(input): return input

def part_1(file): return get_file_size(file, len)

def part_2(file): return get_file_size(file, part_2)

def get_file_size(file, func):
    for i, c in enumerate(file):
        if c == '(':
            width, rep, _ = parse('({:d}x{:d}){}',file[i:]) 
            length = i + len(str(width)+str(rep)) + 3
            return i + get_file_size(file[length + width:], func) + rep * func(file[length: length + width])
    return len(file)