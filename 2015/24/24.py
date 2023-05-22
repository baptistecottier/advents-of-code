from itertools import combinations
import math

def generator(input): 
    return [int(package) for package in input.splitlines()]
    
def part_1(packages): 
    return get_QE(packages, 3)
        
def part_2(packages): 
    return get_QE(packages, 4)

def get_QE(packages, groups):
    target = sum(packages) // groups 
    l = 0
    while l := l + 1:
        for package in combinations(packages,l):
            if sum(package) == target:
                return math.prod(package)
    

    