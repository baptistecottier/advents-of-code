from parse import parse

def generator(input):
    values=[[] for _ in range(len(input.splitlines()))]
    instructions=[None for _ in range(len(input.splitlines()))]

    for instruction in input.splitlines() :
        if 'value' in instruction : 
            value, bot = parse('value {:d} goes to bot {:d}', instruction)
            values[bot].append(value)
        else :
            bot, tl, low, th, high = parse('bot {:d} gives low to {} {:d} and high to {} {:d}', instruction)
            instructions[bot] = [low + 210 * ('output' in tl), high + 210 * ('output' in th )]   
    return (values , instructions)


def part_1(input): return solver(input, 1)


def part_2(input): return solver(input, 2)
    
    
def solver(input, part):
    values, instructions = input
    to_distribute = [(i,sorted(item)) for (i,item) in enumerate(values) if len(item) == 2]
    while to_distribute != [] :
        for i , item in to_distribute :
            if item == [17, 61] : good_bot = i
            for j in [0,1] : values[instructions[i][j]].append(item[j])
            values[i]=[]
        to_distribute = [(i,sorted(item)) for (i,item) in enumerate(values) if len(item) == 2]
    if part == 1: return good_bot
    if part == 2: return values[210][0]*values[211][0]*values[212][0]

