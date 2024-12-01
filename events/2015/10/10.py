from itertools import groupby


def conway(digits, iterations):    
    for _ in range(iterations):
        digits = "".join(f"{len(list(l))}{k}" for k, l in groupby(digits))
    return len(digits)


def solver(digits, iterations = 40):
    yield conway(digits, iterations)
    yield conway(digits, iterations + 10)


