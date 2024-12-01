def preprocessing(puzzle_input):
    return [expr.replace(' ', '') for expr in puzzle_input.splitlines()]


def solver(expressions):
    yield sum(parse(expr) for expr in expressions)
    yield sum(eval("(" + expr.replace('*',')*(') + ')+(0)') for expr in expressions)

def evaluate(s):
    pos = -1

    for i, _ in enumerate(s):
        if i == len(s):
            return evaluate(s)
        if s.count('*') + s.count('+') <= 1:
            return eval(s)
        if pos == -1:
            pos = i
            while s[i] not in '*+':
                i += 1
        else:
            while i <len(s) and str(s[i]).isnumeric():
                i += 1
            s = s.replace(str(s[pos:i]), str(evaluate(s[pos:i])), 1)            

def parse(s):
    while True:
        sum = l_br = r_br = 0
        if all(c not in s for c in '()'):
            return evaluate(s)        
        for i, c in enumerate(s):
            if c == '(': 
                l_br = i
            elif c == ')':
                r_br = i
                sum = evaluate(s[l_br + 1: r_br])
                s = s.replace(str(s[l_br: r_br + 1]), str(sum), 1)
                break
    return 0