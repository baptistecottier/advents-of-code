from parse import parse

def generator(input): 
    return [list(parse("{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.", r))[1:] for r in input.splitlines()]

def part_1(reindeers_infos): 
    return solver(reindeers_infos, old_rule = True) 

def part_2(reindeers_infos): 
    return solver(reindeers_infos, old_rule = False)
    
def solver(reindeers_infos, old_rule):
    n = len(reindeers_infos)
    bonus = [0 for _ in range(n)]
    for second in range(2504, 0, -1):
        ranking = []
        for speed, duration, rest in reindeers_infos: 
            q = second // (duration + rest)
            r = min(duration, second % (duration + rest))
            ranking.append(speed * (r + q * duration))
        if old_rule: 
            return max(ranking)
        for i in range(n):
            bonus[i] += ranking[i] == max(ranking)
    return max(bonus)