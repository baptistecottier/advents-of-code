from math import inf

def preprocessing(input_): 
    return list(int(n) for n in input_), int(input_)

def solver(pattern, length):
    trigger = length + 10
    elves   = (0, 1)
    recipes = [3, 7]
    while True:
        s = sum(recipes[e] for e in elves)
        if s > 9: recipes.append(s // 10)
        recipes.append(s % 10)
        elves = list((e + recipes[e] + 1) % len(recipes) for e in elves)
        if recipes[-6:] == pattern:  
            yield (2, len(recipes) - 6)
            break
        if recipes[-7:-1] == pattern:  
            yield (2, len(recipes) - 7)
            break
    yield (1, ''.join(str(n) for n in recipes[trigger - 10: trigger]))
