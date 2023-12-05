from pythonfw.functions import extract_chunks

def preprocessing(input):
    data = input.split('\n\n')
    seeds = [int(n) for n in data[0].split(' ')[1:]]
    maps = [extract_chunks(mp, 3, func= lambda c : tuple(c)) for mp in data[1:]]
    return seeds, maps

def solver(seeds, maps):
    location = set()
    for seed in seeds:
        for mp in maps:
            for (dst, src, size) in mp:
                if seed in range(src, src + size):
                    seed += (dst - src)
                    break
        location.add(seed)
    yield min(location)

 
    seeds = [seeds[i: i + 2] for i in range(0, len(seeds), 2)]
    maps = maps[::-1]
    loc = 0
    seed = -1

    while (not any(low < seed < low + size for (low, size) in seeds)):
        seed = loc
        for mp in maps:
            for (dst, src, size) in mp:
                if seed in range(dst, dst + size):
                    seed += (src - dst)
                    break 

        loc += 1
    yield loc - 1