from itertools import pairwise


def parser(input_):
    return input_.splitlines()


def solver(strings):
    nice_old_rules = 0
    nice_new_rules = 0
    
    for string in strings:
        
        if any(a == b for a, b in pairwise(string))\
           and sum(string.count(vowel) for vowel in "aeiou") > 2 \
           and not any(pair in string for pair in ('ab','cd','pq','xy')):
                nice_old_rules += 1
                
        length = len(string)
        if any(string.count(pair) > 1 for pair in (string[i: i + 2] for i in range(length - 1))) \
           and any(a == c and a != b for (a, b, c) in (string[i: i + 3] for i in range(length - 2))):
                nice_new_rules += 1
                
    yield nice_old_rules
    yield nice_new_rules


