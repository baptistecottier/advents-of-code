from math      import sqrt
from itertools import permutations, pairwise

def parser(data: str):
    changes: list = list()
    for change in data.splitlines():
        gain: int = int(change.split(' ')[3])
        changes.append(gain if 'gain' in change else -gain)
    return changes

def solver(changes: list[int]):
    def compute_changes(myself):
        n   : int = 1 + int(sqrt(len(changes))) + myself
        best: int = 0
        for arrangement in permutations(range(n)):
            acc: int = 0
            for (a, b) in pairwise(arrangement + (arrangement[0],)):
                if n - myself in (a, b): continue
                i1 :int = (n - 1 - myself) * a + b - (b > a)
                i2 :int = (n - 1 - myself) * b + a - (a > b)
                acc    += changes[i1] + changes[i2]
            if acc > best: best = acc
        return best

    yield compute_changes(myself = False)
    yield compute_changes(myself = True)