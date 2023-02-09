def generator(input):
    state, comb = input.split('\n\n')
    state = state.split(': ')[1]
    combinations = {}
    for c in comb.splitlines():
        prev, post = c.split(' => ')
        combinations[prev] = post
    
    return state, combinations


def part_1(input):
    return solver(input, 20)

def part_2(input): 
    previous = solver(input, 0)
    current = solver(input, 1)
    next = solver(input, 2)
    n = 2
    while next - current != current - previous:
        previous, current = current, next
        next = solver(input, n + 1)
        n += 1
    return solver(input, n) + (next - current) * (50_000_000_000 - n)


def solver(input, gen):
    state, comb = input
    state = '.' * (2 * gen) + state + '.' * (2 * gen)
    next_state = state
    for _ in range(gen):
        state = next_state
        next_state = ''
        for c in range(2, len(state)-2):
            next_state += comb[state[c - 2: c + 3]]
        next_state = '..' + next_state + '..'
    return sum([i - (2 * gen) for i in range(len(next_state)) if next_state[i] == '#'])
