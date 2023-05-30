def generator(input): 
    blacklist = set()
    for element in input.splitlines():
        inf, sup = (int(item) for item in element.split('-'))
        blacklist.add((inf, sup))
    return blacklist

def part_1(intervales): 
    return next_allowed_ip(0, intervales)

def part_2(intervales):  
    counter_ip = 0
    allowed_ip = part_1(intervales)
    while allowed_ip < 4_294_967_295: 
        intervales  = list((inf , sup) for (inf , sup) in intervales if sup > allowed_ip)
        min_ip      = min(intervales, key = lambda item: item[0])[0] 
        counter_ip += min_ip - allowed_ip 
        allowed_ip  = next_allowed_ip(min_ip, intervales)
    return counter_ip


def next_allowed_ip(start, intervales):
    for inf, sup in intervales: 
        if start in range(inf, sup + 1):
            intervales = list((inf, sup) for (inf, sup) in intervales if sup > start)
            return next_allowed_ip(sup + 1 ,intervales)
    return start