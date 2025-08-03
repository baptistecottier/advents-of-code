"""
Advent of Code - Year 2019 - Day 8
https://adventofcode.com/2019/day/8
"""

# Standard imports
from itertools import product

# First party imports
from pythonfw.functions import screen_reader


def preprocessing(puzzle_input: str, image_width: int = 25, image_height: int = 6
                  ) -> dict[int, dict[int, set[tuple[int, int]]]]:
    """
    Processes the puzzle input string into a dictionary of layers, each mapping digits 0-9 to sets
    of (x, y) pixel coordinates based on the specified image width and height.
    """
    image_size = image_width * image_height
    n_layers = len(puzzle_input) // image_size
    layers = {layer: {v: set() for v in range(10)} for layer in range(n_layers)}

    for n, c in enumerate(puzzle_input):
        layers[n // image_size][int(c)].add((n % image_width, (n // image_width) % image_height))
    return layers


def solver(
        layers: dict[int, dict[int, set[tuple[int, int]]]],
        image_width: int = 25,
        image_height: int = 6
        ) -> tuple[int, str]:
    """
    Solves the image layer puzzle by finding the layer with the fewest zeros and decoding the final
    image, yielding both results.
    """
    min_l = min(layers.values(), key=lambda layer: len(layer[0]))

    black = set()
    for pixel in product(range(image_width), range(image_height)):
        layer = 0
        while pixel in layers[layer][2]:
            layer += 1
        if pixel in layers[layer][1]:
            black.add(pixel)

    return len(min_l[1]) * len(min_l[2]), screen_reader(black)
