from collections import defaultdict

def preprocessing(input):
    octopus = defaultdict(set)
    for y, row in enumerate(input.splitlines()):
        for x, n in enumerate(row):
            octopus[int(n)].add((x, y))
    return octopus

def solver(octopus: defaultdict[set]): 
    step    = 0
    flashed = 0
    while len(octopus[0]) != 100: # We assume they all flash simultaneously after the 100th step
        if step == 100: yield flashed
        octopus = defaultdict(set, {n + 1: pos for n, pos in octopus.items()})
        while octopus[10]:
            x, y = octopus[10].pop()
            octopus[0].add((x, y))
            for nx, ny in ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)):
                if (x + nx, y + ny) not in octopus[0]: 
                    for energy in range(1, 10):
                        if (x + nx, y + ny) in octopus[energy]:
                            octopus[energy].remove((x + nx, y + ny))
                            octopus[energy + 1].add((x + nx, y + ny))
                            break
        flashed += len(octopus[0])
        step += 1
    yield step