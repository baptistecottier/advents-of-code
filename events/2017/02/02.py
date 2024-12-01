from itertools  import permutations
from re         import split

def preprocessing(input_):
    lines = [[int(n) for n in split(r'\s', line)] for line in input_.splitlines()]
    return lines

def solver(spreadsheet):
    checksum = 0
    checkdiv = 0
    
    for row in spreadsheet:
        checksum += max(row) - min(row)
        for a, b in permutations(row, 2):
            if a % b == 0: 
                checkdiv += a // b
                break

    yield checksum
    yield checkdiv