from math                  import prod
from re                    import findall
from collections           import defaultdict
from pythonfw.functions    import extract_chunks


def preprocessing(input_): 
    return extract_chunks(input_, 5)


def solver(ingredients):
    nb_ing = len(ingredients)
    frosting, candy, butterscotch, sugar = ingredients + (4 - nb_ing) * [[0, 0, 0, 0, 0]]
    
    frosting     = {i: [i * item for item in frosting]     for i in range(101)}
    candy        = {i: [i * item for item in candy]        for i in range(101)}
    butterscotch = {i: [i * item for item in butterscotch] for i in range(101)}
    sugar        = {i: [i * item for item in sugar]        for i in range(101)}
    scores       = defaultdict(list)
    
    for i in range(101):
        f = frosting[i]
        for j in range(101 - i):
            b = candy[j]
            for k in range(101 - (i + j)):
                c     = butterscotch[k]
                s     = sugar[100 - (i + j + k)]
                score = prod(max(0, sum([v[index] for v in [f, b, c, s]])) for index in range(4))
                scores[sum(v[4] for v in [f, b, c, s])].append(score)

    yield max(sum(scores.values(), []))
    yield max([0, *scores[500]])