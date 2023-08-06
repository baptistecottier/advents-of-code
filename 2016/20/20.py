def preprocessing(input_): 
    blacklist = set()
    for element in input_.splitlines():
        inf, sup = (int(item) for item in element.split('-'))
        blacklist.add((inf, sup))
    return blacklist

def solver(intervales):  
    counter_ip = 0
    allowed_ip =next_allowed_ip(0, intervales)
    yield allowed_ip
    while allowed_ip < 4_294_967_295: 
        intervales  = list((inf , sup) for (inf , sup) in intervales if sup > allowed_ip)
        min_ip      = min(intervales, key = lambda item: item[0])[0] 
        counter_ip += min_ip - allowed_ip 
        allowed_ip  = next_allowed_ip(min_ip, intervales)
    yield counter_ip

def next_allowed_ip(start, intervales):
    for inf, sup in intervales: 
        if start in range(inf, sup + 1):
            intervales = list((inf, sup) for (inf, sup) in intervales if sup > start)
            return next_allowed_ip(sup + 1 ,intervales)
    return start