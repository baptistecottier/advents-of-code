from re import findall
from z3 import If, Optimize, Ints, Int

def preprocessing(puzzle_input):
    nanobots = set()
    numbers = list(map(int, findall(r'-?[0-9]+', puzzle_input)))
    while numbers:
        nanobots.add(((numbers.pop(0), numbers.pop(0), numbers.pop(0)), numbers.pop(0)))
    return nanobots

def solver(puzzle_input):
    yield part_1(puzzle_input)
    yield part_2(puzzle_input)
    
def part_1(nanobots):
    in_range = 0
    max_pos, max_r = max(nanobots, key = lambda n : n[1])
    for pos, _ in nanobots:
        if sum(abs(a - b) for a, b in zip(max_pos, pos)) <= max_r:
            in_range += 1
    return in_range

def part_2(nanobots):
    candidate = Ints("x y z")
    reachable = sum(If(z3_dist(pos, candidate) <= r, 1, 0) for pos, r in nanobots)
    
    opt = Optimize()
    opt.maximize(reachable)
    opt.minimize(z3_dist((0,0,0), candidate))
    opt.check()
    
    model = opt.model()
    return sum(abs(model[n].as_long()) for n in candidate)
    
            

def z3_abs(x): 
    return If(x >= 0, x, -x)

def z3_dist(x, y):
    return sum(If(a - b >= 0, a - b, b - a) for a, b in zip(x, y))

