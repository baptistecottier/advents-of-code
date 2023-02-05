from copy import deepcopy

def generator(input): 
    return [[int(item) for item in component.split('/')] for component in input.splitlines()]
        
def part_1(input): 
    return max(solver(deepcopy(input), 0, [(0,0)]), key = lambda x : x[1])[1]

def part_2(input): 
    return max(solver(deepcopy(input), 0, [(0, 0)]))[1]


def solver(components, port, strength):
    candidates = [c for c in components if port in c]
    if candidates == [] : return strength
    for c in candidates:
        cc = deepcopy(components)
        cc.remove(c)
        strength += solver(cc, sum(c)-port, [(strength[0][0]+1, strength[0][1]+sum(c))])
    return strength