parser = int

def solver(input):
    pos   = 0
    state = [0]
    for i in range(50_000_000):
        pos = 1 + (pos + input) % (i + 1)
        if pos == 1 : value = i + 1
        if i < 2017 : state.insert(pos, i + 1)
        if i == 2017: 
            yield state[state.index(2017) + 1]
    yield value