from itertools import combinations

def generator(input):
    return tuple(int(container) for container in input.splitlines())

def part_1(containers): 
    size = 0
    good_combination = 0
    while size < len(containers):
        for comb in combinations(containers, size := size + 1):
            if sum(comb) == 150:
                good_combination += 1
    return good_combination

def part_2(containers): 
    size = 0
    good_combination = 0
    while good_combination == 0:
        for comb in combinations(containers, size := size + 1):
            if sum(comb) == 150: 
                good_combination += 1
    return good_combination