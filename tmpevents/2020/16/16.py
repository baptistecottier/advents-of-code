from parse     import parse
from itertools import chain
from math      import prod 

def preprocessing(input):
    p_rules, p_ticket, p_nearby = input.split('\n\n')
    rules = []
    for rule in p_rules.splitlines():
        _, a, b, c, d = list(parse("{}: {:d}-{:d} or {:d}-{:d}", rule))
        rules.append(list(chain(range(a, b+1), range(c, d+1))))
    ticket = [int(item) for item in p_ticket.splitlines()[1].split(',')]
    nearby = [[int(item) for item in n.split(',')] for n in p_nearby.splitlines()[1:]]
    return rules, ticket, nearby
        
def solver(rules, ticket , nearby):
    counter, nearby = invalid_detector(rules, nearby)
    yield counter 
    
    candidates = [[i for i in range(len(ticket)) if all([n[i] in r for n in nearby])] for r in rules]
    while any([len(c) != 1 for c in candidates]):
        for c in candidates:
            if len(c) == 1:
                for cc in candidates:
                    if cc != c and c[0] in cc: cc.remove(c[0])
    yield prod(ticket[candidates[i][0]] for i in range(6))

def invalid_detector(rules, nearby):
    valid = list(chain(*rules))
    cnt = sum(sum(v for v in n if v not in valid) for n in nearby)
    nearby = [n for n in nearby if all(item in valid for item in n)]
    return cnt, nearby