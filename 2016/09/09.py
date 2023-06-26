from parse import parse

def parser(data): return data

def solver(file): 
    yield get_file_size(file, len)
    yield get_file_size(file, rec := lambda x: get_file_size(x, rec))


def get_file_size(file, func):
    for i, c in enumerate(file):
        if c == '(':
            width, rep, _ = parse('({:d}x{:d}){}',file[i:]) 
            length = i + len(str(width)+str(rep)) + 3
            return i + get_file_size(file[length + width:], func) + rep * func(file[length: length + width])
    return len(file)