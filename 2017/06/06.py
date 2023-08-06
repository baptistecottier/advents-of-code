from copy import deepcopy

def parser(input): 
    return list(int(item) for item in input.split())

def solver(input):
    met_banks = redistributions(input) 
    yield len(met_banks)-1
    yield len(met_banks[:-1]) - met_banks[:-1].index(met_banks[-1])

def redistributions(input):
    n = len(input)
    bank = input
    met_banks = [] 
    while bank not in met_banks: 
        met_banks.append(deepcopy(bank))
        to_distribute = max(bank)
        i = bank.index(to_distribute)
        bank[i] = 0
        for j in range(n): 
            bank[j] += to_distribute // n + ((j - (i + 1)) % n < (to_distribute % n))
    met_banks.append(bank)
    return met_banks
    