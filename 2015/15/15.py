from math                  import prod
from re                    import findall
from collections           import defaultdict
from aoctools.functions    import extract_chunks


def parser(input_): 
    return extract_chunks(input_, 5)


def solver(ingredients):
    frosting, candy, butterscotch, sugar = ingredients
    butterscotch = {i: [i * item for item in butterscotch] for i in range(101)}
    candy        = {i: [i * item for item in candy]        for i in range(101)}
    frosting     = {i: [i * item for item in frosting]     for i in range(101)}
    sugar        = {i: [i * item for item in sugar]        for i in range(101)}
    scores       = defaultdict(list)
    
    for i in range(100):
        f = frosting[i]
        for j in range(100 - i):
            b = butterscotch[j]
            for k in range(100 - (i + j)):
                c     = candy[k]
                s     = sugar[100 - (i + j + k)]
                score = prod(max(0, sum([v[index] for v in [f, b, c, s]])) for index in range(4))
                scores[sum(v[4] for v in [f, b, c, s])].append(score)

    yield max(sum(scores.values(), []))
    yield max(scores[500])