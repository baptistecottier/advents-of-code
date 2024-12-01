from collections import Counter
from itertools   import pairwise


def preprocessing(puzzle_input): 
    return (int(item) for item in puzzle_input.split('-'))


def solver(bounds):
    min, max = bounds
    cnt_eq: int = 0
    cnt_ge: int = 0

    for pw in range(min, max + 1):
        if not any([a > b for (a, b) in pairwise(str(pw))]):
            values = [n for (_, n) in Counter(str(pw)).most_common() if n > 1]
            if values: cnt_ge += 1
            if 2 in values: cnt_eq += 1

    yield cnt_ge
    yield cnt_eq