def generator(input):
    return [line.split(' ') for line in input.splitlines()]
        
def part_1(input):
    register = {'a': 0,'b': 0,'f': 0,'i': 0,'p': 0}
    d = input[0]
    i = 0
    while input[i][0] != 'rcv':
        d = input[i]
        match d[0]:
            case 'snd': sound_frequency = interpret(d[1], register)
            case 'set': register[d[1]] = interpret(d[2], register)
            case 'add': register[d[1]] += interpret(d[2], register) 
            case 'mul': register[d[1]] *= interpret(d[2], register)
            case 'mod': register[d[1]] %= interpret(d[2], register)
            case 'rcv': 
                if register[d[1]] != 0: register[d[1]] = sound_frequency
            case 'jgz': 
                if interpret(d[1], register) != 0: i += int(d[2]) - 1
        i += 1
    return sound_frequency

def part_2(input):
    register = [{'a': 0,'b': 0,'f': 0,'i': 0,'p': 0}, {'a': 0,'b': 0,'f': 0,'i': 0,'p': 1}]
    queue =[[], []]
    p = 1
    i = [0,0]
    cnt = 0 
    while 1:
        d = input[i[p]]
        match d[0]:
            case 'snd': 
                cnt += p
                queue[1-p].insert(0, interpret(d[1], register[p]))
            case 'set': register[p][d[1]]  = interpret(d[2], register[p])
            case 'add': register[p][d[1]] += interpret(d[2], register[p]) 
            case 'mul': register[p][d[1]] *= interpret(d[2], register[p])
            case 'mod': register[p][d[1]] %= interpret(d[2], register[p])
            case 'rcv': 
                if 0 not in i and queue == [[],[]]: return cnt
                elif queue[p] == []: 
                    p = 1 - p
                    i[p] -= 1
                else: register[p][d[1]] = queue[p].pop()
            case 'jgz': 
                if interpret(d[1], register[p]) > 0: i[p] += interpret(d[2], register[p]) - 1
        i[p] += 1

    
def interpret(val,register):
     if val.isalpha(): return register[val]
     else: return int(val)