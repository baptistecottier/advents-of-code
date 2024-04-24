def preprocessing(puzzle_input):
    state, comb = puzzle_input.split('\n\n')
    state = state.split(': ')[1]
    combinations = {}
    for c in comb.splitlines():
        prev, post = c.split(' => ')
        combinations[prev] = post
    return state, combinations

def solver(state, spread):
    previous_sum  = sum_pots(previous:= generate(state,    spread), 1)
    current_sum   = sum_pots(current:=  generate(previous, spread), 2)
    next_sum      = sum_pots(next:=     generate(current,  spread), n:= 3)
    cycles        = 0
    
    while 2 * current_sum != next_sum + previous_sum:
        cycles += 1
        if cycles == 19: yield current_sum
        previous_sum, current_sum = current_sum, next_sum
        next_sum = sum_pots(next:= generate(next, spread), n:= n + 1)
    yield next_sum + (next_sum - current_sum) * (50_000_000_000 - n)


def generate(state, spread):
    return ''.join([spread['.' * (5 - n) + state[:n]] for n in range(1, 5)] + \
                   [spread[state[n: n + 5]]           for n in range(len(state) - 4)] +\
                   [spread[state[n - 5:] + '.' * n]   for n in range(1, 5)])

def sum_pots(state, generations):
    return sum(i - 2 * generations for i, p in enumerate(state) if p == '#')