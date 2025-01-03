from itertools import permutations

def preprocessing(data) : 
    return data.splitlines()

def solver(operations, start = "abcdefgh"): 
    yield scramble(list(start), operations)

    for word in permutations(start):
        if scramble(word, operations) == 'fbgdceah' : 
            yield ''.join(word)
            break


def scramble(pw, instructions):
    for inst in instructions : 
        command , details = inst.split(' ', 1)
        pw = list(pw)
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

