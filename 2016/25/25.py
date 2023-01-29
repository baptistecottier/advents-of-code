def generator(input): 
    return [line.split(' ') for line in input.splitlines()]

def interpret(val,register):
     if val.isalpha(): return register[val]
     else : return int(val)

def solver(instructions, a):
    cnt, tictac, i = 0, 0, 0
    register={'a' : a , 'b' : 0 , 'c' : 0 , 'd': 0}

    while(0 <= i < len(instructions)) :
        ordre, details = instructions[i][0] , instructions[i][1:]
        match ordre : 
            case "cpy" : register[details[1]] = interpret(details[0],register)
            case 'dec': register[details[0]]-=1
            case 'inc': register[details[0]]+=1
            case 'jnz': i+=(interpret(details[0] , register) != 0) * (interpret(details[1] , register) - 1)
            case _ : 
                if tictac == interpret(details[0], register) :
                    if cnt > 10 : return a
                    tictac = not tictac
                    cnt += 1
                else : return 0
        i += 1

def part_1(input):
    a , signal= 0 , 0
    while signal == 0 : 
        signal = solver(input, a)
        a += 1
    return signal

def part_2(input): return "Signal can be retransmitted"