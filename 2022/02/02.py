def preprocessing(input):
    duels = {(p, q): 0 for p in range(3) for q in range(1, 4)}
    for duel in input.splitlines():
        adv, me = duel.split(' ')
        adv = int(ord(adv)) - 65
        me  = int(ord(me)) - 87
        duels[(adv, me)] += 1
    return duels 

def solver(duels):
    total_score = 0
    real_score  = 0
    for (adv, me), rep in duels.items():
        total_score += rep * (me + 3 * ((me - adv) % 3))
        real_score  += rep * (3 * me - 2 + (me + 1 + adv) % 3)
    yield total_score
    yield real_score