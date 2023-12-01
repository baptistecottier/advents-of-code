def preprocessing(input): 
    return {n: input.count(str(n)) for n in range(9)}

def solver(lanternfishes):
    for day in range(256):
        if day == 80: yield sum(lanternfishes.values())
        lanternfishes[9]  = lanternfishes[0]
        lanternfishes[7] += lanternfishes[0]
        lanternfishes     = {n: lanternfishes[n + 1] for n in range(9)}
    yield sum(lanternfishes.values())