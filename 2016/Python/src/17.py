import itertools
import sys

with open("Day17/input.txt") as f:
    stuff = [int(x) for x in f.read().splitlines()]
    count=0
    stop=0
    for L in range(0, len(stuff)+1):
        for subset in itertools.combinations(stuff, L):
            if sum(list(subset))==150 : 
                stop=1
                count += 1
        if stop==1 :
            print(count)
            sys.exit()