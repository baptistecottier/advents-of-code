from collections        import defaultdict
from pythonfw.functions import extract_chunks, sign


def preprocessing(input): 
    return extract_chunks(input, 4)


def solver(vents):
    visited  = defaultdict(int)
    diagonal = defaultdict(int)
    
    for (sx, sy, ex, ey) in vents:
        if sx == ex: 
            for pos in ((sx, y) for y in range(min(sy, ey), 1 + max(sy, ey))):
                visited[pos] += 1
        elif sy == ey: 
            for pos in ((x, sy) for x in range(min(sx, ex), 1 + max(sx, ex))):
                visited[pos] += 1
        else: 
            dx, dy = sign(ex - sx), sign(ey - sy)
            for pos in ((sx + k * dx, sy + k * dy) for k in range(abs(sx - ex) + 1)):
                diagonal[pos] += 1
    
    keys = set(visited.keys())
    yield sum(visited.get(k) > 1 for k in keys)
    
    keys.update(diagonal.keys())
    yield sum((visited.get(k, 0) + diagonal.get(k, 0)) > 1 for k in keys)
