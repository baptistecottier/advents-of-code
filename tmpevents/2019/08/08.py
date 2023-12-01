from itertools          import product
from pythonfw.functions import screen_reader

def preprocessing(input):
    layers = {l: {'0': set(), '1': set(), '2': set()} for l in range(len(input) // 150) }
    for n, c in enumerate(input): layers[n // 150][c].add((n % 25, (n // 25) % 6))
    return layers

def solver(layers):
    min_l = min(layers.values(), key = lambda l: len(l['0']))
    yield len(min_l['1']) * len(min_l['2'])
    
    black = set()
    for pixel in product(range(25), range(6)):
        l = 0
        while pixel in layers[l]['2']: l += 1
        if pixel in layers[l]['1']: black.add(pixel)
    yield screen_reader(black)