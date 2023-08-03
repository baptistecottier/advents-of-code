from itertools import combinations
from math      import prod


def parser(input_): 
    return [int(package) for package in input_.splitlines()]
    

def solver(packages): 
    yield get_QE(packages, 3)
    yield get_QE(packages, 4)


def get_QE(packages, groups):
    target = sum(packages) // groups 
    size = 1
    while True:
        for package in combinations(packages,size):
            if sum(package) == target:
                return prod(package)
        size += 1

    