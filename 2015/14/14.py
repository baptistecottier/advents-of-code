from parse import parse

def generator(input) : 
    return [list(parse("{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.", r))[1:] for r in input.splitlines()]

def part_1(input) : 
    return solver(input, new_rule = False) 

def part_2(input) : 
    return solver(input, new_rule = True)
    
def solver(input, new_rule) :
    bonus = [0 for _ in range(len(input))]
    for s in range(2503-2502 * new_rule, 2504):
        ranking = []
        for speed, duration, rest in input : 
            q = s // (duration + rest)
            r = min(duration, s % (duration + rest))
            ranking.append(speed * (r + q * duration))
        bonus = [sum(x)  for x in zip(bonus, [item==max(ranking) for item in ranking])]
    return [max(ranking) , max(bonus)][new_rule]