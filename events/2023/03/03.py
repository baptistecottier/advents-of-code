from itertools      import product
from collections    import defaultdict
from re             import finditer

def preprocessing(input): 
    numbers = set()
    symbols = defaultdict(list)
    for y, line in enumerate(input.splitlines()):
        for match in finditer(r'[0-9]+', line):
            numbers.add((match.span(), y, int(match.group())))
        for x, c in enumerate(line):
            if c not in "1234567890.": 
                symbols[c].append((x, y))
    return numbers, symbols
        

def solver(numbers, symbols): 
    sum_part_numbers = 0
    sum_gear_ratios  = 0
    gears = {}
    for ((start, end), y, n) in numbers:
        for (tx, ty) in product(range(start - 1, end + 1), range(y - 1, y + 2)):
            if (tx, ty) in sum(symbols.values(), list()):
                sum_part_numbers += n
                if (tx, ty) in symbols['*']:
                    if (tx, ty) in gears: 
                        sum_gear_ratios += gears[(tx, ty)] * n
                    else: gears[(tx, ty)] = n

    yield sum_part_numbers
    yield sum_gear_ratios
