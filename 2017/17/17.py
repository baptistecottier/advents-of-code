def generator(input): return int(input)

def part_1(input):
    p=0
    state = [0]
    for i in range(2017):
        p = 1 + (p + input) % (i + 1)
        state.insert(p, i+1)
    return state[state.index(2017)+ 1]
    
def part_2(input):
    p=0
    for i in range(50_000_000):
        p = 1 + (p + input) % (i + 1)
        if p == 1 : value = i + 1
    return value