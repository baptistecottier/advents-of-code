def preprocessing(input):
    values = [int(item) for item in input.split(',')]
    return ({spoken:[n] for (n, spoken) in enumerate(values)} , values[-1])

def solver(spoken, last_spoken):
    for i in range(len(spoken),30_000_000):
        if i == 2_020: yield last_spoken
        if len(spoken[last_spoken]) == 1: 
            last_spoken = 0
        else: 
            p, n = spoken[last_spoken]
            last_spoken = n - p
        if last_spoken in spoken: 
            spoken[last_spoken] = [spoken[last_spoken][-1], i]
        else: 
            spoken[last_spoken] = [i]
    yield last_spoken

