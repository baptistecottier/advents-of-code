import functools

def generator(input) : 
    list_input = [eval(l) for l in input.replace('\n\n', '\n').splitlines()]
    return list_input
        
def part_1(input) : 
    orders = [((i + 1) * is_pair_sorted(input[2 * i] , input[2 * i + 1])) for i in range(len(input)//2)]
    return sum(orders)

def part_2(input) : 
    sorted_list = sorted(input+[[2] , [6]] , key = functools.cmp_to_key(make_comparator(is_pair_sorted)))
    return (sorted_list.index([2]) + 1) * (sorted_list.index([6]) + 1)
               
def is_pair_sorted(a, b) :
    if type(a)==list and type(b)==list :
        if a == [] : return True
        elif b == [] : return False
        elif a[0] == b[0] : return is_pair_sorted(a[1:], b[1:])
        else : return is_pair_sorted(a[0] , b[0])
    elif type(a)==list and type(b)==int  : return is_pair_sorted(a, [b])
    elif type(a)==int  and type(b)==list : return is_pair_sorted([a], b)
    else : return a < b

def make_comparator(my_cmp):
    def compare(x, y):
        if my_cmp(x, y): return -1
        elif my_cmp(y, x): return 1
        else: return 0
    return compare