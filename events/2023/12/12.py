def preprocessing(puzzle_input):
    records = list()
    for conditions, pattern in (line.split(' ') for line in puzzle_input.splitlines()):
        pattern = [int(p) for p in pattern.split(',')]
        records.append((conditions, pattern))
    return sorted(records, key = lambda x : len(x[0]))

from itertools import product 

def test(records, rep = 0):
    cnt = 0
    for condition, pattern in records:
        condition += f'?{condition}' * rep
        pattern   += rep * pattern
        nb_jokers  = condition.count('?')
        k = condition.count('#')
        for jokers in product(['#', '.'], repeat = nb_jokers):
            if jokers.count('#') != sum(pattern) - k: continue
            c = condition
            j = list(jokers)
            while j:
                c = c.replace('?', j.pop(), 1)
            if c.count('#') == sum(pattern):
                test = [item.count('#') for item in c.split('.') if item != '']
                if test == pattern: cnt += 1
    return cnt

def solver(records):
    yield test(records)
    yield test(records, 4) # Theoritically correct
