from itertools import permutations

def generator(input) : return input.splitlines()

def part_1(operations): 
    return scramble('abcdefgh', operations)

def part_2(operations): 
    for word in permutations('abcdefgh'):
        if scramble(word, operations) == 'fbgdceah' : 
            return ''.join(word)


def scramble(pw, instructions):
    for inst in instructions : 
        command , details = inst.split(' ', 1)
        match command :
            case 'swap': 
                _, x, _, _, y = details.split(' ')
                if 'position' in details : 
                    x, y = int(x), int(y)
                    pw[x], pw[y] = pw[y], pw[x]
                else :
                    pw = list((''.join(pw)).replace(x, '_').replace(y,x).replace('_',y))

            case 'rotate' : 
                if 'based' in details : 
                    x    = pw.index(details[-1])
                    step = 1 + x + ( x >= 4 )
                else : 
                    direction, x = details.split(' ')[:2]
                    if direction == 'right':
                        step = int(x)
                    else: 
                        step = - int(x)
                temp = pw
                pw   = [temp[(i - step) % len(pw)] for i in range(len(pw))]
            
            case 'reverse' : 
                _ , x , _, y = details.split(' ')
                x , y = int(x), int(y)
                pw    = pw[:x] + pw[x: y + 1][::-1] + pw[y + 1:]

            case 'move' : 
                _, x, _, _, y = details.split(' ')
                x, y = int(x), int(y)
                t    = pw[x]            
                pw   = pw[:x] + pw[x + 1:]
                pw   = pw[:y] + [t] + pw[y:]
    return ''.join(pw)

