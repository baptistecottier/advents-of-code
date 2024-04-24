from pythonfw.classes import Register

def preprocessing(puzzle_input):
    return [line.split(' ') for line in puzzle_input.splitlines()]

def solver(puzzle_input): 
    yield (1, part_1(puzzle_input))
    yield (2, part_2(puzzle_input))
    
def part_1(puzzle_input):
    reg = Register({'a': 0,'b': 0,'f': 0,'i': 0,'p': 0})
    d = puzzle_input[0]
    i = 0
    while puzzle_input[i][0] != 'rcv':
        d = puzzle_input[i]
        match d[0]:
            case 'snd': sound_frequency = reg.get(d[1])
            case 'set': reg[d[1]] = reg.get(d[2])
            case 'add': reg[d[1]] += reg.get(d[2])
            case 'mul': reg[d[1]] *= reg.get(d[2])
            case 'mod': reg[d[1]] %= reg.get(d[2])
            case 'rcv': 
                if reg[d[1]] > 0: reg[d[1]] = sound_frequency
            case 'jgz': 
                if reg.get(d[1]) != 0: i += int(d[2]) - 1
        i += 1
    return sound_frequency

def part_2(puzzle_input):
    reg = [Register({'a': 0,'b': 0,'f': 0,'i': 0,'p': 0}), 
           Register({'a': 0,'b': 0,'f': 0,'i': 0,'p': 1})]
    queue =[[], []]
    p = 1
    i = [0,0]
    cnt = 0 
    while 1:
        d = puzzle_input[i[p]]
        match d[0]:
            case 'snd': 
                cnt += p
                queue[1-p].insert(0, reg[p].get(d[1]))
            case 'set': reg[p][d[1]]  = reg[p].get(d[2])
            case 'add': reg[p][d[1]] += reg[p].get(d[2]) 
            case 'mul': reg[p][d[1]] *= reg[p].get(d[2])
            case 'mod': reg[p][d[1]] %= reg[p].get(d[2])
            case 'rcv': 
                if 0 not in i and queue == [[],[]]: return cnt
                elif queue[p] == []: 
                    p = 1 - p
                    i[p] -= 1
                else: reg[p][d[1]] = queue[p].pop()
            case 'jgz': 
                if reg[p].get(d[1]) > 0: i[p] += reg[p].get(d[2]) - 1
        i[p] += 1