def generator(input):
    return [expr.replace(' ', '') for expr in input.splitlines()]

from itertools import product

def part_1(input):
    cnt = 0  
    for expr in input: 
        for (x, y) in product(range(10), repeat = 2):
            expr = expr.replace(str(x)+' + '+str(y), '('+str(x)+' + '+str(y)+')')
        cnt += eval(expr)
    return cnt

def part_2(input): return sum(eval("("+l.replace('*',')*(') + ')+(' + "0)") for l in input)

import re 

def evaluate(s):
    s = s.replace('(','').replace(')','') # don't need brackets now    
    pos = oper = -1

    for i, _ in enumerate(s): # store bracket pos, find numbers
        if i == len(s):
            return evaluate(s)
        if s.count('*') + s.count('+') <= 1:
            return eval(s)
        if pos == -1:
            pos = i # pos of 1st number
            while s[i] not in '*+':
                oper=i
                i+=1
        elif oper > -1:
            while str(s[i]).isnumeric():
                if (i := i + 1) == len(s):
                    break
            s = s.replace(str(s[pos:i]), str(evaluate(s[pos:i])), 1)            

def parse(s):
    while True:
        sum = l_br = r_br = 0
        if s.count('(') + s.count(')') == 0: # no brackets, skip processing
            return evaluate(s)        
        for i, j_ in enumerate(s):
            if s[i] == '(': # store brackets position
                l_br = i
            elif s[i] == ')': # found closing bracket
                r_br = i
                sum = evaluate(s[l_br:r_br+1]) # evaluate expression
                s = s.replace(str(s[l_br:r_br+1]), str(sum), 1)
                break
    return 0