"""Advent of Code - Year 2017 - Day 21"""

from itertools import product

def preprocessing(puzzle_input: str) -> dict[str, str]:
    """
    Process the puzzle input to create a dictionary of pattern transformations.
    
    Each line in the input represents a rule with a pattern and its replacement. The function
    generates all possible orientations (rotations and flips) of each pattern and maps all of
    them to the same replacement in the rules dictionary.
    
    Args:
        puzzle_input: String containing puzzle input with rules in the format
                     "pattern => replacement" where patterns and replacements use '/' as
                     row delimiters.
    
    Returns:
        Dictionary mapping each possible pattern orientation to its replacement.
    """
    rules = {}
    for line in puzzle_input.splitlines():
        pattern, replacement = line.replace('/','').split(' => ')
        r1, r2, r3 = rotate(pattern, 1),  rotate(pattern, 2),  rotate(pattern, 3)
        f, f1, f2, f3 = flip(pattern), flip(r1), flip(r2) , flip(r3)
        for p in [pattern, r1, r2, r3, f, f1, f2, f3]:
            rules[p]=replacement
    return rules


def flip(pixels: str) -> str:
    """
    Flip the input pixels horizontally, returning a new string.
    """
    size = int(len(pixels) ** 0.5)
    return ''.join([''.join(pixels[i * (size): i * size + size])[::-1] for i in range(size)])


def rotate(pixels: str, n: int) -> str:
    """
    Rotate the pixels string n times using predefined permutation indexes
    """
    perm = [[2,0,3,1], [6,3,0,7,4,1,8,5,2]]
    for _ in range(n):
        size = int(len(pixels) ** 0.5) - 2
        pixels =''.join([pixels[perm[size][i]] for i in range(len(pixels))])
    return pixels


def solver(rules: dict[str, str], iterations: int = 18):
    """
    Solves the fractal art puzzle by applying enhancement rules to a grid over multiple iterations.
    
    The function starts with a 3x3 grid ('.#...####') and repeatedly applies the given
    enhancement rules. For each iteration, it divides the grid into smaller squares (2x2 or 3x3),
    enhances each square according to the rules, and then combines the enhanced squares to form 
    a new grid.
    
    Args:
        rules: A dictionary mapping patterns to their enhanced versions
        iterations: The number of iterations to perform (default: 18)
        
    Yields:
        int: The number of '#' characters (pixels on) in the grid after 5 iterations
        int: The number of '#' characters (pixels on) in the grid after all iterations
    """
    grid = '.#...####'
    for m in range(iterations):
        size = int(len(grid) ** 0.5)

        if size % 2 == 0:
            divisor = 2
        else: divisor = 3
        enhanced_grid = []

        for r, c in product(range(size // divisor), range(size // divisor)):
            index = (r * size + c) * divisor
            mini_grid = ''

            for i in range(divisor):
                mini_grid += grid[index: index + divisor]
                index += size
            enhanced_grid.append(rules[mini_grid])

        grid = ''
        for i in range(size + size // divisor):
            ii = (i * (divisor + 1)) % (divisor + 1) ** 2
            jj = (i // (divisor + 1)) * (size // divisor)
            for j in range(size // divisor):
                grid += enhanced_grid[jj + j][ii: ii + (divisor + 1)]

        if m == 4:
            yield grid.count('#')
    yield grid.count('#')
