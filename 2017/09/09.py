from re import sub


def preprocessing(input_):                                               
    return sub(r'\!.', '', input_)


def solver(record): 
    step       = 0
    score      = 0
    garbage    = 0
    garb_count = 0
    
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