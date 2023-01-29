from itertools import permutations

def generator(input) : return input.splitlines()

def part_1(input): return solver('abcdefgh', input)

def part_2(input): 
    for word in permutations('abcdefgh'):
        if solver(word, input)=='fbgdceah' : return ''.join(word)


def solver(pw, instructions):
    for inst in instructions : 
        command , details = inst.split(' ', 1)
        match command :
            case 'swap': 
                _ , x , _ , _ , y = details.split(' ')
                if 'position' in details : 
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
                pw=pw[:y]+t+pw[y:]
    return ''.join(pw)

