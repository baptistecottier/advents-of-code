from copy import deepcopy

def parser(input): 
    return [[int(item) for item in component.split('/')] for component in input.splitlines()]
        

def solver(connections): 
    bridges = build_bridges(connections, 0, [(0,0)])
    yield max(bridges, key = lambda x: x[1])[1]
    yield max(bridges)[1]

def build_bridges(components, port, strength):
    candidates = [c for c in components if port in c]
    if not candidates: return strength
    for c in candidates:
        cc = deepcopy(components)
        cc.remove(c)
        strength += build_bridges(cc, sum(c)-port, [(strength[0][0]+1, strength[0][1]+sum(c))])
    return strength