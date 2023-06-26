from itertools import combinations
import math

def parser(input): 
    return [int(package) for package in input.splitlines()]
    
def solver(packages): 
    yield get_QE(packages, 3)
    yield get_QE(packages, 4)

def get_QE(packages, groups):
    target = sum(packages) // groups 
    size = 1
    while True:
        for package in combinations(packages,size):
            if sum(package) == target:
                return math.prod(package)
        size += 1

    