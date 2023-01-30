from re import findall
from copy import deepcopy

def generator(input): 
    return [int(item) for item in findall('[0-9]+', input)]

def part_1(input):
    return len(solver(input))-1
        
def part_2(input): 
    met_banks = solver(input) 
    return len(met_banks[:-1]) - met_banks[:-1].index(met_banks[-1])


def solver(input):
    n = len(input)
    bank = input
    met_banks = [] 
    while bank not in met_banks : 
        met_banks.append(deepcopy(bank))
        to_distribute = max(bank)
        i = bank.index(to_distribute)
        bank[i] = 0
        for j in range(n):
            bank[j] += to_distribute // n + ((j - (i + 1)) % n < (to_distribute % n))
    met_banks.append(bank)
    return met_banks
    