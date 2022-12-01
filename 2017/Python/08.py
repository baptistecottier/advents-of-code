from parse import parse
from AoC_tools import read_input

instructions=read_input().splitlines()

reg={}
op={'inc':1, 'dec':-1}

# registers initialisation
for instruction in instructions :
    r , _ = instruction.split(' ', 1)
    reg[r]=0
max_reg=0
# instructions execution
for instruction in instructions :
    r1, sign, step, r2, cond = parse('{:l} {:l} {:d} if {:l} {}', instruction)
    if eval(str(reg[r2])+cond): 
        reg[r1]+=op[sign]*step
        max_reg=max(max_reg,reg[r1])

print(max([reg[item] for item in reg]) , max_reg)