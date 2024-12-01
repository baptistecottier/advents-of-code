from itertools          import product
from pythonfw.functions import screen_reader


def preprocessing(puzzle_input, image_width = 25, image_height = 6):
    image_size = image_width * image_height
    n_layers = len(puzzle_input) // image_size
    layers = {l: {v: set() for v in range(10)} for l in range(n_layers)}
    for n, c in enumerate(puzzle_input): layers[n // image_size][int(c)].add((n % image_width, (n // image_width) % image_height))
    return layers


def solver(layers, image_width = 25, image_height = 6):
    min_l = min(layers.values(), key = lambda l: len(l[0]))
    yield len(min_l[1]) * len(min_l[2])
    
    black = set()
    for pixel in product(range(image_width), range(image_height)):
        layer = 0
        while pixel in layers[layer][2]: layer += 1
        if pixel in layers[layer][1]: black.add(pixel)
    yield screen_reader(black)