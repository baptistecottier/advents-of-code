from AoC_tools import read_input

instructions=read_input().splitlines()

def scramble(input):
    pw=input
    for inst in instructions : 
        command , details = inst.split(' ', 1)
        match command :
            case 'swap': 
                _ , x , _ , _ , y = details.split(' ')
                if 'position' in details : #position X with position Y 
                    x , y = list(map(int,[x,y]))
                    pw[x] , pw[y] = pw[y] , pw[x]
                else :
                    pw=list((''.join(pw)).replace(x, '_').replace(y,x).replace('_',y))

            case 'rotate' : 
                if 'based' in details : 
                    x=pw.index(details[-1])
                    step=1+x+(x>=4)
                else : 
                    direction , x = details.split(' ')[:2]
                    step = (-1 + 2 *(direction=='right')) * int(x)
                temp=pw
                pw=[temp[(i-step)% len(pw)] for i in range(len(pw))]
            
            case 'reverse' : 
                _ , x , _, y = details.split(' ')
                x , y = list(map(int,[x,y]))
                pw = pw[:x]+pw[x:y+1][::-1]+pw[y+1:]

            case 'move' : 
                _, x, _, _, y = details.split(' ')
                x , y = list(map(int,[x,y]))
                t=pw[x]            
                pw=pw[:x]+pw[x+1:]
                pw=pw[:y]+list(t)+pw[y:]
    return ''.join(pw)

print('Scrambling \'abcdefgh\' results in', '\''+scramble('abcdefgh')+'\'')

from itertools import permutations

for input in permutations('abcdefgh'):
    if scramble(input)=='fbgdceah' : 
        print('Unscrambling \'fbgdceah\' results in','\'' + ''.join(input) + '\'') 
        break
