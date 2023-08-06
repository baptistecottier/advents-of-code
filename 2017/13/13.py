from math import lcm

def parser(input):
    return [[int(i) for i in item.split(': ')] for item in input.splitlines()]

def solver(record):
    pairs = list((layer, 2 * (depth - 1)) for layer, depth in record)
    severity = 0
    for layer, depth in pairs: 
        if layer % depth == 0: severity += layer * (depth // 2 + 1)
    yield severity

    delay = 1
    while(any((delay + layer) % depth == 0  for layer, depth in pairs)): delay += 1
    yield delay
