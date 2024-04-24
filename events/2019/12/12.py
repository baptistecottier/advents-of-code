from math                import lcm
from pythonfw.classes    import Particule
from pythonfw.functions  import extract_chunks, sign

def preprocessing(puzzle_input: str) -> set[Particule]:
    moons: set[Particule] = {Particule(*moon) for moon in extract_chunks(puzzle_input, 3)}
    return moons
        
def solver(moons: set[Particule]):
    coord: list   = ['x', 'y', 'z']
    visited: dict = {c: {(tuple(getattr(m.p, c), 0) for m in moons)} for c in coord}
    cycles: dict  = dict()
    step: int     = 0
    
    while len(cycles) < 3 or step <= 1_000:
        if step == 1_000: 
            yield sum(moon.p.manhattan() * moon.v.manhattan() for moon in moons)
            for c in cycles.keys(): coord.remove(c)
            
        for c in coord:
            for m, g in zip(moons, gravity(moons, c)):
                setattr(m.v, c, getattr(m.v, c) + g)
                setattr(m.p, c, getattr(m.p, c) + getattr(m.v, c))
                
            values = tuple((getattr(m.p, c), getattr(m.v, c)) for m in moons)
            if values in visited[c] and c not in cycles: 
                cycles[c] = step
                coord.remove(c)
            else: 
                visited[c].add(values)
            
        step += 1
    
    yield lcm(*cycles.values())

def gravity(moons: list[Particule], attr: str) -> tuple[int]:
    return tuple(sum(sign(getattr(a.p, attr) - getattr(b.p, attr)) for a in moons) for b in moons)