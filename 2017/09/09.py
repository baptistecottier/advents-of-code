import re

def generator(input):                                               
     return re.sub(r'\!.', '', input)

def part_1(input):
    return solver(input, 0)

def part_2(input):
    return solver(input, 1)


def solver(input, i): 
    garb_count, garbage, score, step= 0, 0, 0, 0
    for char in input:
        match (garbage, char):
            case (1, '>'): garbage = 0
            case (0, '<'): garbage = 1
            case (0, '{'): score, step = score + step + 1, step + 1
            case (0, '}'): step = step - 1
            case (0, _): pass
            case _: garb_count += 1
    return [score, garb_count][i]