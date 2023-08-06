from itertools          import permutations
from pythonfw.functions import extract_chunks

def preprocessing(input_):
    return extract_chunks(input_, 16)

def solver(spreadsheet):
    yield (1, sum(max(row) - min(row) for row in spreadsheet))
    yield (2, sum(sum(a // b for a, b in permutations(row, 2) if a % b == 0) for row in spreadsheet))