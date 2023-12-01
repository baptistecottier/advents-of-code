from itertools import combinations


def preprocessing(input_):
    return tuple(int(container) for container in input_.splitlines())


def solver(*containers):
    total = 0
    found = False
    
    for size in range(len(containers)):
        size_total = sum(sum(comb) == 150 for comb in combinations(containers, size))
        if not found and size_total != 0: 
            found = True
            yield (2, size_total)
        total += size_total
    
    yield (1, total)