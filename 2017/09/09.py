import re

def preprocessing(input_):                                               
    return re.sub(r'\!.', '', input_)

def solver(record): 
    garb_count, garbage, score, step= 0, 0, 0, 0
    for char in record:
        match (garbage, char):
            case (1, '>'): garbage = 0
            case (0, '<'): garbage = 1
            case (0, '{'): score, step = score + step + 1, step + 1
            case (0, '}'): step = step - 1
            case (0, _): pass
            case _: garb_count += 1
    yield score
    yield garb_count