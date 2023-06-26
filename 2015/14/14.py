from aoctools import extract_chunks

def parser(data: str): 
    return extract_chunks(data, 3)
    
def solver(reindeers_infos: list[int]):
    bonus: list[int] = [0 for _ in reindeers_infos]
    
    for second in range(1, 2504):
        ranking: list = list()
        for speed, duration, rest in reindeers_infos: 
            q: int = second // (duration + rest)
            r: int = min(duration, second % (duration + rest))
            ranking.append(speed * (r + q * duration))
        for i, rank in enumerate(ranking):
            bonus[i] += rank == max(ranking)
            
    yield max(ranking)
    yield max(bonus)