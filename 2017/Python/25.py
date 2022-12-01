with open('inputs/25.txt') as f:
    instructions=f.read().splitlines()

def interpret(val,register):
     if val.isalpha():
        return register[val]
     else : return int(val)

def execute(a):
    cnt=0
    tictac=0
    register={'a' : a , 'b' : 0 , 'c' : 0 , 'd': 0}
    i=0
    while(0 <= i < len(instructions)) :
        instruction=instructions[i] 
        ordre , details = instruction.split(' ',1)

        if ordre == 'cpy' : 
            src , dst = details.split(' ')
            register[dst] = interpret(src,register)
            i+=1

        elif ordre == 'dec' :  
            register[details]-=1
            i+=1

        elif ordre == 'inc' :  
            register[details]+=1
            i+=1

        elif ordre == 'jnz' :
            reg , step = details.split(' ')
            if interpret(reg , register) != 0 : i+=interpret(step , register)
            else : i+=1

        else : 
            if tictac == interpret(details, register) :
                if cnt > 100 : return a
                tictac = 1 - tictac
                i , cnt = i+1 , cnt + 1
            else : return 0

a , signal= 300 , 0
while signal==0 :
    signal=execute(a)
    a-=1
print('Part I:', signal)