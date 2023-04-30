def generator(input):
    values = [int(item) for item in input.split(',')]
    return ({spoken :[n] for (n, spoken) in enumerate(values)} , values[-1])

def part_1(input): return solver(input, 2020)

def part_2(input): return solver(input, 30_000_000)

def solver(input, turns):
    spoken, last_spoken = input
    for i in range(len(spoken),turns):
        if len(spoken[last_spoken]) == 1: 
            last_spoken = 0
        else: 
            p, n = spoken[last_spoken]
            last_spoken = n - p
        if last_spoken in spoken: 
            spoken[last_spoken] = [spoken[last_spoken][-1], i]
        else : 
            spoken[last_spoken] = [i]
    return last_spoken

