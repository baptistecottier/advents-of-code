from statistics import mean, median

def preprocessing(puzzle_input): 
    return [int(item) for item in puzzle_input.split(',')]

def solver(crabs):
    med_crabs  = int(median(crabs))
    med_fuel   = 0
    mean_crabs = round(mean(crabs))
    mean_fuel  = 0
    
    for crab in crabs:
        med_fuel  += abs(crab - med_crabs)
        distance   = abs(crab - mean_crabs)
        mean_fuel += distance * (distance + 1) // 2
        
    yield med_fuel
    yield mean_fuel