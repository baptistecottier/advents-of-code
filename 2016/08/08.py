import re
from itertools import product

def generator(input):
    sequence = []
    for seq in input.splitlines():
        data = re.split('[\sx=]', seq)
        match data[0], data[1]:
            case "rect", _:       sequence.append((0, int(data[1]),  int(data[2])))
            case "rotate", "row": sequence.append((1, int(data[-3]), int(data[-1])))
            case "rotate", _:     sequence.append((2, int(data[-3]), int(data[-1])))
    return sequence
    
def part_1(sequence): return get_code(sequence).count('█')

def part_2(sequence): return get_code(sequence)  


def get_code(sequence): 
    w, h = 50, 6
    screen = [[' ' for _ in range(w)] for _ in range(h)]
    for op, a, b in sequence: 
        match op: 
            case 0: 
                for x, y in product(range(a), range(b)): 
                    screen[y][x] = '█' 
            case 1: 
                screen[a] = screen[a][-b:] + screen[a][:-b]
            case 2: 
                temp = [screen[y][a] for y in range(h)]
                for y in range(h) : 
                    screen[y][a] = temp[(y - b) % h]
    return '\n'.join(''.join(line) for line in screen)