from math               import lcm
from pythonfw.functions import extract_chunks


def preprocessing(input_):
    return extract_chunks(input_, 2)


def solver(record):
    pairs = list((layer, 2 * (depth - 1)) for layer, depth in record)
    severity = 0
    
    for layer, depth in pairs: 
        if layer % depth == 0: severity += layer * (depth // 2 + 1)
    yield severity

    delay = 1
    while(any((delay + layer) % depth == 0  for layer, depth in pairs)): delay += 1

    yield delay
