def generator(input): return input

def part_1(input): return solver(input, 40)

def part_2(input): return solver(input, 400_000)

def tile_type(left, right):
    if (left == right) : return '.'
    else : return '^'


def solver(input, rep):
    s='.'+input+'.'
    safe_tiles=s.count('.')-2
    for t in range(rep - 1):
        s='.'+''.join([tile_type(s[i]=='^',s[i+2]=='^') for i in range(len(s)-2)])+'.'
        safe_tiles+=s.count('.')-2
    return safe_tiles