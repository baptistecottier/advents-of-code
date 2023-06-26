from itertools import pairwise

def parser(data):
    return data.splitlines()

def solver(strings):
    counter = 0
    for string in strings:
        if  any(a == b for a, b in pairwise(string)) and \
            sum(string.count(vowel) for vowel in "aeiou") > 2 and \
            not any(pair in string for pair in ('ab','cd','pq','xy')):
                counter += 1
    yield counter

    counter = 0
    for string in strings:
        length = len(string)
        if  any(string.count(pair) > 1 for pair in (string[i:i+2] for i in range(length - 1))) and \
            any(a == c and a != b for (a, b, c) in (string[i:i+3] for i in range(length - 2))):
                counter += 1
    yield counter


