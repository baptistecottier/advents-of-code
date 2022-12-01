from math import prod
from AoC_tools import chinese_remainder
from parse import parse

with open("inputs/15.txt") as input :
    lines=input.read().splitlines()

a , n = [], []
for line in lines : 
    d , tn , ta = parse('Disc #{:d} has {:d} positions; at time=0, it is at position {:d}.',line)
    n.append(tn) # Extracting the moduli
    a.append(-(ta+d)) # As the start position is k, it remains -k positions. 

crt=chinese_remainder(n, a)
print(crt-2,'...', crt-1, '...' ,  crt ,'PRESS NOW!!! Got it!! Come on, just one more...')

# Disc #7 has 11 positions; at time=8, it is at position 0
crt =  chinese_remainder([prod(n),11] , [crt,-7])
print(crt-2,'...', crt-1, '...' ,  crt ,'PRESS NOW!!! Ok, that\'s enough.')
