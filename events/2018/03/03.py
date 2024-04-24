from collections        import defaultdict
from itertools          import product
from pythonfw.functions import extract_chunks

def preprocessing(puzzle_input):
    claims = extract_chunks(puzzle_input, 5)
    return claims

def solver(claims):
    visited = defaultdict(int)
    for ida, xa, ya, dxa, dya in claims:
        for tx, ty in product(range(xa, xa + dxa), range(ya, ya + dya)):
            visited[(tx, ty)] += 1
        if all(xa - xb > dxb or \
               xb - xa > dxa or \
               ya - yb > dyb or \
               yb - ya > dya for idb, xb, yb, dxb, dyb in claims if idb != ida):
            yield (2, ida)
        
    yield (1, sum(n > 1 for n in visited.values()))
