# import re

# with open("Day18/input") as f:
#     terms=[eval(term) for term in f.read().splitlines()]

def magnitude(value):
    if type(value)==int:
        return value
    else : return 3*magnitude(value[0]) + 2*magnitude(value[1])


# def snail_sum(term1, term2):
#      return [term1 , term2]

# def split(value):
#     txt=str(value)
#     numbers=[int(item) for item in re.findall(r'\d+', txt) if int(item)>9]
#     for item in numbers:
#         txt=txt.replace(str(item), str([item//2 , item//2 + item %2]))
#     return eval(txt)

# def find_reg_number(value):
#     matches = re.finditer(r'(?=((\[\d,\[)|(\],\d\])))',value)
#     results = [int(match.group(1).strip('[],')) for match in matches]
#     print(results)

# def sub_explode(pair, txt):
#     before, after = txt.split(txt)
#     lb=find_reg_number(before)
#     la=find_reg_number(after)
#     if lb != []:
#         if la != []:
#             b=lb[-1]
#             a=lb[0]
#             txt.replace(pair, 0)
# def depth(txt):
#     return txt.count('[')-txt.count(']')+1
        

# def explode(value):
#     txt=str(value)
#     pairs=re.findall(r'\[\d, \d\]',txt)
#     for pair in pairs:
#         txt.find(r'\[\d, ')
    
# find_reg_number("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
        



# # value=[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]

# # print(explode(value))

# #print(sum([magnitude(term) for term in terms]))

#!/usr/bin/env python3

import itertools

def add_left(x, n):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [add_left(x[0], n), x[1]]


def add_right(x, n):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [x[0], add_right(x[1], n)]


def explode(x, n=4):
    if isinstance(x, int):
        return False, None, x, None
    if n == 0:
        return True, x[0], 0, x[1]
    a, b = x
    exp, left, a, right = explode(a, n - 1)
    if exp:
        return True, left, [a, add_left(b, right)], None
    exp, left, b, right = explode(b, n - 1)
    if exp:
        return True, None, [add_right(a, left), b], right
    return False, None, x, None


def split(x):
    if isinstance(x, int):
        if x >= 10:
            return True, [x // 2, x // 2 + x % 2]
        return False, x
    a, b = x
    change, a = split(a)
    if change:
        return True, [a, b]
    change, b = split(b)
    return change, [a, b]


def add(a, b):
    x = [a, b]
    while True:
        change, _, x, _ = explode(x)
        if change:
            continue
        change, x = split(x)
        if not change:
            break
    return x


with open("Day18/input") as f:
    lines = list(map(eval, f.read().splitlines()))
    value=lines[0]
    for line in lines[1:]: value=add(value,line)
    print("Part I:", magnitude(value))
    print("Part II:", max(magnitude(add(a, b)) for a, b in itertools.permutations(lines, 2)))