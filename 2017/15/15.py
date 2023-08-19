from itertools import count


def preprocessing(input_):
    return [int(line.rsplit(' ')[-1]) for line in input_.splitlines()]


def solver(generators): 
    a, b        = generators
    old_count   = []
    new_count_a = []
    new_count_b = []
    
    while len(old_count) < 40_000_000 and all(len(count) < 5_000_000 for count in (new_count_a, new_count_b)):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
                         
        old_count.append((a - b) % (2 ** 16) == 0)
        if a % 4 == 0: new_count_a.append(a)
        if b % 8 == 0: new_count_b.append(b)

    yield sum(old_count)
    yield sum((a - b) % (2 ** 16) == 0 for a, b in zip(new_count_a, new_count_b))
