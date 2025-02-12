from pythonfw.functions import extract_chunks


def preprocessing(input_): 
    return extract_chunks(input_, 3, neg = False)

    
def solver(reindeers_infos, t = 2504):
    bonus = [0 for _ in reindeers_infos]
    
    for second in range(1, int(t)):
        ranking = list()
        for speed, duration, rest in reindeers_infos: 
            q = second // (duration + rest)
            r = min(duration, second % (duration + rest))
            ranking.append(speed * (r + q * duration))
            
        best = max(ranking)
        for i, rank in enumerate(ranking):
            if rank == best: bonus[i] += 1
            
    yield max(ranking)
    yield max(bonus)