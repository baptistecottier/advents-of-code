def generator(input): 
    blacklist = []
    for element in input.splitlines():
        inf, sup = [int(item) for item in element.split('-')] 
        blacklist.append((inf, sup))
    return blacklist

def part_1(input): return next_allowed_ip(0, input)

def part_2(input):  
    allowed_ip=0
    i = part_1(input)
    while i < 4294967295 : 
        input=[(inf , sup) for (inf , sup) in input if sup >  i ] 
        min_ip=min(input , key = lambda item : item[0])[0] 
        allowed_ip += min_ip - i 
        i = next_allowed_ip(min_ip, input)
    return allowed_ip


def next_allowed_ip(start ,intervales):
    for inf , sup in intervales : 
        if start in range(inf, sup+1) :
            intervales=[(inf , sup) for (inf , sup) in intervales if sup >  start] 
            return next_allowed_ip(sup+1 ,intervales)
    return start