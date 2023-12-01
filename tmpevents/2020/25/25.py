def preprocessing(input):
    return (int(item) for item in input.splitlines())

def solver(integers):
    p, q  = integers
    e = 0
    n = 1
    while n not in (p, q):
        n = (n * 7) % 20201227
        e += 1
    if n == p: yield pow(q, e, 20201227)
    if n == q: yield pow(p, e, 20201227)