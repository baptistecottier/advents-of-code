from itertools import permutations
from parse import parse
from math import prod
with open('inputs/10.txt') as f:
    instructions=f.read().splitlines()

inst_bot,inst_values = [] , []
for instruction in instructions :
    if 'value' in instruction : inst_values.append(instruction)
    else : inst_bot.append(instruction)

list_bot=[]

bots_instructions=[[0,0] for _ in range(231)] # Stocking distribution instructions. 210 bots + 21 outputs
for inst in inst_bot:
    bot , low , high = parse('bot {} gives low to {} and high to {}', inst) # Extract informations

    l=int(low.split(' ')[1])
    if 'output' in low : l+=210 # If the recveiver is an ouput, go to the outputs part of the array

    h=int(high.split(' ')[1])
    if 'output' in high : h+=210 # If the recveiver is an ouput, go to the outputs part of the array

    bots_instructions[int(bot)]=[l,h] # We add the lower and higher value redirection 

bots_comparison=[[] for x in range(231)] # Stocking microship emplacement
for inst in inst_values:
    value, bot=parse('value {:d} goes to bot {:d}', inst)
    bots_comparison[bot].append(value)

while any([len(cmp)==2 for cmp in bots_comparison[:210]]): # While at least a bot contains two values to compared ...
    for bot in bots_comparison: # Find the bot with two values
        if len(bot) == 2 : 
            i=bots_comparison.index(bot) # Retrieve the bot index
            bot=sorted(bot)
            if bot==[17,61] : # Answer to Part I
                    print('The number of the bot that is responsible for comparing value-61 microchips with value-17 microchips is', i)
            bots_comparison[bots_instructions[i][0]].append(bot[0]) # Distribution of microships
            bots_comparison[bots_instructions[i][1]].append(bot[1])
            bots_comparison[i]=[] # Emptying of the bot
print('and the product of the values of one chip in each of outputs 0, 1, and 2 is' ,prod([item[0] for item in bots_comparison[210:213]]))
