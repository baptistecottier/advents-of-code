def generator(input) :
    duels = []
    for duel in input.splitlines():
        [a, b] = duel.split(' ')
        duels.append([ord(a) - 63 , ord(b) - 88])
    return duels

def part_1(input) :
    return solver(input , real_rules = False)

def part_2(input) :
    return solver(input , real_rules = True)

def solver(input, real_rules) :
    s = 0
    for [a, b] in input :
        v = [(b + (2 - real_rules) * a) % 3 , b]
        s += 1 + 3 * v[real_rules] + v[1 - real_rules]
    return s
