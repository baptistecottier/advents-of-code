from collections import defaultdict
from math        import prod
from re          import findall
from aoctools    import extract_chunks

def parser(data: str): 
    return extract_chunks(data, 5)


def solver(ingredients):
    frosting, candy, butterscotch, sugar = ingredients
    butterscotch: dict = {i: [i * item for item in butterscotch] for i in range(101)}
    candy       : dict = {i: [i * item for item in candy]        for i in range(101)}
    frosting    : dict = {i: [i * item for item in frosting]     for i in range(101)}
    sugar       : dict = {i: [i * item for item in sugar]        for i in range(101)}
    scores      : dict = defaultdict(list)
    
    for i in range(100):
        f: list[int] = frosting[i]
        for j in range(100 - i):
            b: list[int] = butterscotch[j]
            for k in range(100 - (i + j)):
                c    : list[int] = candy[k]
                s    : list[int] = sugar[100 - (i + j + k)]
                score: int       = prod(max(0, sum([v[index] for v in [f, b, c, s]])) for index in range(4))
                scores[sum(v[4] for v in [f, b, c, s])].append(score)

    yield max(sum(scores.values(), []))
    yield max(scores[500])