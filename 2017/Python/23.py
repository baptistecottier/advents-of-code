import time

with open('inputs/23.txt') as input: 
    instructions=input.read().splitlines()

register={'a' : 7 , 'b' : 0 , 'c' : 0 , 'd': 0}

def interpret(val):
     if val.isalpha():
        return register[val]
     else : return int(val)

i=0
cpt=0
while(0 <= i < len(instructions)) :
    cpt+=1
    instruction=instructions[i] 

    ordre , details = instruction.split(' ',1)

    if ordre == 'tgl' :
        x=register[details]
        if 0 <= i+x < len(instructions):
            if len(instructions[i+x].split(' '))==2 :
                if 'inc' in instructions[i+x] : instructions[i+x]='dec'+instructions[i+x][3:]
                else : instructions[i+x]='inc'+instructions[i+x][3:]

            else : 
                if 'jnz' in instructions[i+x] : instructions[i+x]='cpy'+instructions[i+x][3:]
                else : instructions[i+x]='jnz'+instructions[i+x][3:]
        
        i+=1

    elif ordre == 'cpy' : 
        src , dst = details.split(' ')
        register[dst] = interpret(src)
        i+=1

    elif ordre == 'dec' :  
        register[details]-=1
        i+=1

    elif ordre == 'inc' :  
        register[details]+=1
        i+=1

    else : # ordre = 'jnz'
        reg , step = details.split(' ')
        if interpret(reg) != 0 : i+=interpret(step)
        else : i+=1


print('Part I', register['a'])