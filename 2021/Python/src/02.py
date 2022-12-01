from AoC_tools import read_input
from parse import parse 

instructions=read_input().splitlines()
Part_I={'x' : 0 , 'depth' : 0 , 'aim' : 0}
Part_II={'x' : 0 , 'depth' : 0 , 'aim' : 0}

for instruction in instructions:
    command,number = parse('{:l} {:d}', instruction)
    match command :
        case 'forward': 
            Part_I['x']+=number
            Part_II['x']+=number
            Part_II['depth']+=Part_II['aim']*number
        case 'down' : 
            Part_I['depth']+=number
            Part_II['aim']+=number
        case 'up': 
            Part_I['depth']-=number
            Part_II['aim']-=number

for score in [Part_I, Part_II]:
    print(score['x'] * score['depth'])