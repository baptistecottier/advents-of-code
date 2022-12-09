def generator(input) : 
    return input

def part_1(input) : 
    return input.count('(') - input.count(')')

def part_2(input) : 
    floor = 0
    for i in range(len(input)) :
        if input[i]=='(' : floor += 1
        else : floor -= 1
        if floor < 0 : return i+1
    