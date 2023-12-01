def preprocessing(input_): 
    return list(int(item) for item in input_.split())


def solver(state):
    visited, last = redistributions(state) 
    cycles = len(visited)
    yield cycles
    yield cycles - visited.index(last)


def redistributions(bank):
    n   = len(bank)
    met = []
    
    while bank not in met: 
        met.append(bank.copy())
        to_distribute = max(bank)
        i = bank.index(to_distribute)
        bank[i] = 0
        for j in range(n): 
            bank[j] += to_distribute // n + ((j - (i + 1)) % n < (to_distribute % n))

    return met, bank
    