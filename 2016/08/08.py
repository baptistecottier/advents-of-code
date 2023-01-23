import re
from itertools import product

def generator(input):
    ops = []
    for op in input.splitlines():
        numbers = [int(item) for item in re.findall('[0-9]+',op)]
        if 'rect' in op : ops.append((2,numbers[0],numbers[1]))
        else: ops.append(('x' in op,numbers[0],numbers[1]))
    return ops


def solver(input): 
    w, h = 50, 6
    screen = [[' ' for _ in range(w)] for _ in range(h)]
    for op, a, b in input : 
        match op: 
            case 0: screen[a]=screen[a][-b:]+screen[a][:-b]
            case 1: 
                temp = [screen[y][a] for y in range(h)]
                for y in range(h) : screen[y][a]=temp[(y-b) % h]
            case 2: 
                for x,y in product(range(a), range(b)): screen[y][x]='█' 
    return '\n'.join([''.join(line) for line in screen])
    
    
def part_1(input): return solver(input).count('█')

def part_2(input): return solver(input)  

        