def generator(input) :
    return [[ord(duel.split(' ')[0]) - 63 , ord(duel.split(' ')[1]) - 88] for duel in input.splitlines()]

def part_1(input) :
    return solver(input , real_rules = False)

def part_2(input) :
    return solver(input , real_rules = True)

def solver(input, real_rules) :
    return sum([1 + 3 * [(b + (1 + real_rules) * 2 * a) % 3 , b][real_rules] + [(b + (1 + real_rules) * 2 * a) % 3 , b][not real_rules] for [a, b] in input])