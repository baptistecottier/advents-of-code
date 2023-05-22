from math import sqrt
from itertools import permutations, pairwise

def generator(input): 
    changes = []
    for change in input.splitlines():
        gain = int(change.split(' ')[3])
        if 'gain' in change: 
            changes.append(gain)
        else:
            changes.append(-gain)
    return changes

def part_1(changes):
    return compute_changes(changes, me = False)

def part_2(changes): 
    return compute_changes(changes, me = True)


def compute_changes(changes, me):
    best = 0
    n = 1 + int(sqrt(len(changes))) + me
    changes += [0 for _ in range(n)]
    for arrangement in permutations(range(n)):
        acc = 0
        for (a, b) in pairwise(arrangement + (arrangement[0],)):
            if n - me in (a, b): continue
            i1 = (n - 1 - me) * a + b - (b > a)
            i2 = (n - 1 - me) * b + a - (a > b)
            acc += changes[i1] + changes[i2]
        if acc > best: best = acc
    return best
            
