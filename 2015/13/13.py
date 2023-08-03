from math      import sqrt
from itertools import permutations, pairwise


def parser(input_):
    changes = list()
    for change in input_.splitlines():
        gain = int(change.split(' ')[3])
        changes.append(gain if 'gain' in change else -gain)
    return changes


def solver(changes):
    
    def compute_changes(myself):
        n    = 1 + int(sqrt(len(changes))) + myself
        best = 0
        for arrangement in permutations(range(n)):
            acc = 0
            for (a, b) in pairwise(arrangement + (arrangement[0],)):
                if n - myself in (a, b): continue
                i1 = (n - 1 - myself) * a + b - (b > a)
                i2 = (n - 1 - myself) * b + a - (a > b)
                acc    += changes[i1] + changes[i2]
            if acc > best: best = acc
        return best

    yield compute_changes(myself = False)
    yield compute_changes(myself = True)