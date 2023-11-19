from pythonfw.functions import sign


def preprocessing(input): 
    data = []
    
    for line in input.replace(':','').splitlines():
        details = line.split(' ')
        data.append(details)
        if details[0] == 'root': left, right = details[1], details[3]
    
    return data, left, right


def solver(monkeys, left, right):
    yield int(root_yell(monkeys, None, left, right))

    min_bound, max_bound = 0, 1_000_000_000_000_000
    delta_humn = None
    
    while delta_humn != 0:
        humn = (min_bound + max_bound) // 2
        delta_humn = root_yell(monkeys, humn, left, right)
        
        delta_min_bound = root_yell(monkeys, min_bound, left, right)
        
        if delta_min_bound == delta_humn: min_bound = max_bound
        max_bound = humn
    yield humn
           
             
def root_yell(mnks, humn, left, right): 
    monkeys = {}
    
    if humn != None: monkeys['humn'] = humn
    
    while len(monkeys) != len(mnks):
        for details in mnks:
            v_out = details[0]
            v_in = details[1:]
            if monkeys.get(v_out) == None:
                if len(v_in) == 1: 
                    monkeys[v_out] = int(v_in[0])
                elif all(monkeys.get(v_in[i]) != None for i in [0, 2]):
                    a = monkeys[v_in[0]]
                    b = monkeys[v_in[2]]
                    match v_in[1]:
                        case '+': monkeys[v_out] = a + b
                        case '-': monkeys[v_out] = a - b
                        case '*': monkeys[v_out] = a * b
                        case '/': monkeys[v_out] = a / b
                        
    if humn == None: return  monkeys[left] + monkeys[right]
    else: return sign(monkeys[left] - monkeys[right])
