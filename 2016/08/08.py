import re
from itertools import product
from aoctools import screen_to_word
def parser(input):
    sequence = []
    for seq in input.splitlines():
        data = re.split('[\sx=]', seq)
        match data[0], data[1]:
            case "rect", _:       sequence.append((0, int(data[1]),  int(data[2])))
            case "rotate", "row": sequence.append((1, int(data[-3]), int(data[-1])))
            case "rotate", _:     sequence.append((2, int(data[-3]), int(data[-1])))
    return sequence
   
def solver(sequence): 
    w, h = 50, 6
    screen = set()
    for op, a, b in sequence: 
        match op: 
            case 0: 
                screen.update({(x, y) for x, y in product(range(a), range(b))})
            case 1: 
                screen = {(x if y != a else (x + b) % w, y) for (x, y) in screen}
            case 2: 
                screen = {(x, y if x != a else (y + b) % h) for (x, y) in screen}

    yield len(screen)
    yield screen_to_word(screen)
