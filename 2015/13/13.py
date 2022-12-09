from itertools import permutations, pairwise

def generator(input) : 
    return [(-1) ** ('lose' in rule) * int(rule.split(' ')[3]) for rule in input.splitlines()]

def part_1(input) :
    return solver(input, me = False)

def part_2(input) : 
    return solver(input, me = True)

def solver(input, me) :
    best = 0
    n = int(len(input) ** 0.5) + 1 + me
    for arrangement in permutations(range(n)):
        acc = 0
        for (a,b) in pairwise(arrangement + (arrangement[0],)):
            if n-me not in (a,b) :
                i1 = (n - 1 - me) * a + b - (b>a)
                i2 = (n - 1 - me) * b + a - (a>b)
                acc += input[i1] + input[i2]
        best = max(best, acc)
    return best
            
