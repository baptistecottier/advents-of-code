from math import log

nb_elves=5

# For explanations, see : https://youtu.be/uCsD3ZGzMgE
log2 = int(log(nb_elves,2))
winner = nb_elves % (2 ** log2) 
winner = 2 * winner + 1
print(winner)
print('When taking the present of the first elf on the left, the elf', winner, 'will have all the presents')

# The following steps have been deduced after a long and extremely difficult analysis
log3=int(log(nb_elves,3))
survivor=nb_elves % (3 ** log3)
if 2 < nb_elves / (3 ** log3) < 3  : survivor += 3 ** log3 + survivor
print('while taking the present of the elf directly across the circle makes win the elf', survivor)
