from itertools import product

def preprocessing(puzzle_input): 
    return puzzle_input.splitlines()

def solver(boxids):
    len_id = len(boxids[0])
    twice  = 0
    thrice = 0
    bound  = - 1
    for ida in boxids: 
        counts  = set(ida.count(c) for c in ida)
        twice  += 2 in counts
        thrice += 3 in counts
        for idb in boxids[:bound]:
            common = list(a for a, b in zip(ida, idb) if a == b)
            if len(common) == len_id - 1:
                yield (2, ''.join(common))
                bound = 0
    yield (1, twice * thrice)