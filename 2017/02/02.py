from itertools          import permutations
from pythonfw.functions import extract_chunks


def preprocessing(input_):
    return extract_chunks(input_, 16)


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