import itertools
import math
import sys

def generator(input) : 
    return [int(package) for package in input.splitlines()]
    
def part_1(packages) : 
    return solver(packages, 3)
        
def part_2(packages) : 
    return solver(packages, 4)

def solver(packages, groups) :
    target = sum(packages) // groups 
    minQE = sys.maxsize
    found = False
    l = 0
    while not found:
        for package in itertools.combinations(packages,l) :
            if sum(package) == target :
                found = True
                minQE = min(minQE, math.prod(package))
        l += 1
    return minQE
    

    