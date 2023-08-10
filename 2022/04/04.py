from pythonfw.functions import extract_chunks

def preprocessing(input_):
    return extract_chunks(input_, 4, neg = False)

def solver(pairs):
    contained = 0
    overlap   = 0
    for (s1, e1, s2, e2) in pairs:
        if (s2 - s1) * (e2 - e1) <= 0:
            contained += 1
        if (e2 - s1) * (s2 - e1) <= 0:
            overlap += 1
    yield contained
    yield overlap