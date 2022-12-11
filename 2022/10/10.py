
def generator(input) : 
    reg=[]
    v = 1
    for i in input.splitlines() : 
        reg.append(v)
        if "addx" in i : 
            reg.append(v)
            v += int(i.split(' ')[1])
    return reg
            
            
def part_1(input) : 
    return sum([x * input[x-1] for x in [20, 60, 100, 140, 180, 220]])

def part_2(input) :
    dsp = [" ", "■"]
    crt = [dsp[ i % 40 in [v-1 , v, v+1]]+((i % 40) == 39)*'\n' for i, v in enumerate(input)]
    return "".join(crt)[:-1]