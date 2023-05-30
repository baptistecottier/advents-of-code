from math import prod
from re   import findall

def generator(input):
    values    = list(int(item) for item in findall(r'[0-9]+', input))
    equations = set()
    while values:
        ta, _, tn, d = values.pop(), values.pop(), values.pop(), values.pop()
        equations.add((-(ta + d), tn))
    return equations

def part_1(equations): 
    return chinese_remainder(equations)

def part_2(equations: set): 
    equations.add((-7, 11))
    return chinese_remainder(equations)


def chinese_remainder(equations):
    sum     = 0
    product = prod(modulo for _, modulo in equations)
    for remainder, modulo in equations:
        sub_product = product // modulo
        sum        += remainder * pow(sub_product, -1, modulo) * sub_product
    return sum % product