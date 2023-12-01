from functools          import cmp_to_key
from pythonfw.functions import sign


def preprocessing(input): 
    list_input = [eval(l) for l in input.replace('\n\n', '\n').splitlines()]
    return list_input


def solver(packets): 
    orders = [((i + 1) * is_pair_sorted(packets[2 * i] , packets[2 * i + 1])) for i in range(len(packets)//2)]
    yield sum(orders)
    
    packets = sorted(packets + [[2] , [6]], key = cmp_to_key(lambda x, y: sign(x, y, is_pair_sorted)), reverse = True)
    yield (packets.index([2]) + 1) * (packets.index([6]) + 1)


def is_pair_sorted(a, b):
    if type(a)==list and type(b)==list:
        if a == []: return True
        elif b == []: return False
        elif a[0] == b[0]: return is_pair_sorted(a[1:], b[1:])
        else: return is_pair_sorted(a[0] , b[0])
    elif type(a)==list and type(b)==int : return is_pair_sorted(a, [b])
    elif type(a)==int  and type(b)==list: return is_pair_sorted([a], b)
    else: return a < b