def generator(input) : 
    list_input = []
    for l in input.replace('\n\n', '\n').splitlines() :
        list_input.append(eval(l))
    return list_input
        
def part_1(input) : 
    scores = []
    for i in range(len(input)//2) : 
        a = input[2*i]
        b = input[2*i+1]
        scores.append((i + 1) * is_pair_sorted(a , b))
    return sum(scores)

import functools

def part_2(input) : 
    
    lll = sorted(input+[[2] , [6]] , key = functools.cmp_to_key(make_comparator(is_pair_sorted)))
    aa = lll.index([2]) + 1
    bb = lll.index([6]) + 1
    return aa * bb
               
def is_pair_sorted(a, b) :
    if type(a)==int and type(b)==int : return a < b
    elif type(a)==list and type(b)==list :
        if a == [] : return True
        elif b == [] : return False
        elif a[0] == b[0] : return is_pair_sorted(a[1:], b[1:])
        else : return is_pair_sorted(a[0] , b[0])
    elif type(a)==int and type(b)==list :
        return is_pair_sorted([a], b)
    elif type(a)==list and type(b)==int :
        return is_pair_sorted(a, [b])

def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare
        
        