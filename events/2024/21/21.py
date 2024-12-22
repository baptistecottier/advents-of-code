from itertools   import pairwise
from collections import defaultdict


def preprocessing(puzzle_input):
    numpad = {'7': (0, 0), '8': (1, 0), '9': (2, 0),
              '4': (0, 1), '5': (1, 1), '6': (2, 1),
              '1': (0, 2), '2': (1, 2), '3': (2, 2),
                           '0': (1, 3), 'A': (2, 3)}

    codes = []
    for raw_code in puzzle_input.splitlines():
        code = [(2, 3)] + [numpad[c] for c in raw_code]
        buttons = "A"
        for (xa, ya), (xb, yb) in pairwise(code):
            (dx, dy) = (xb - xa, yb - ya)
            padding = (dy * "v") + (-dy * "^") + (dx * ">") + (-dx * "<")
            if (dx > 0 and dy > 0 and (xa, yb) == (0, 3)) or \
               (dx < 0 and dy < 0 and (xb, ya) != (0, 3)):
                    buttons += padding[::-1] + "A"
            else:
                    buttons += padding + "A"
        dict_buttons = defaultdict(int)
        for i in range(len(buttons)-1):
            dict_buttons[buttons[i: i+2]] += 1
        codes.append((int(raw_code[:-1]), dict_buttons))
    return codes


def get_presses(buttons: dict):
    presses = {
        "<>": ["A>", ">>", ">A"]      ,"<v": ["A>", ">A"], 
        "<^": ["A>", ">^", "^A"]      ,"<A": ["A>", ">>", ">^", "^A"],
        "><": ["A<", "<<", "<A"]      ,">v": ["A<", "<A"],
        ">^": ["A<", "<^", "^A"]      ,">A": ["A^", "^A"],
        "v<": ["A<", "<A"]            ,"v>": ["A>", ">A"],
        "v^": ["A^", "^A"]            ,"vA": ["A^", "^>", ">A"],
        "^<": ["Av", "v<", "<A"]      ,"^>": ["Av", "v>", ">A"],
        "^v": ["Av", "vA"]            ,"^A": ["A>", ">A"],
        "A<": ["Av", "v<","<<", "<A"] ,"A>": ["Av", "vA"],
        "Av": ["A<", "<v", "vA"]      ,"A^": ["A<", "<A"],
        "<<": ["AA"]                  ,">>": ["AA"],
        "vv": ["AA"]                  ,"^^": ["AA"],
        "AA": ["AA"]
        }
    dir_presses = defaultdict(int)
    for pair, occurences in buttons.items():
        for step in presses[pair]:
            dir_presses[step] += occurences
    return dir_presses

        
def solver(codes_buttons):
    yield count_presses(codes_buttons, 2)
    yield count_presses(codes_buttons, 25)
   
    
def count_presses(buttons, n_robots):
    complexity = 0
    for n, buttons in buttons:
        for _ in range(n_robots):
            buttons = get_presses(buttons)
        complexity += n * sum(buttons.values())
    return complexity