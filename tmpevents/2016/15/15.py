from re       import findall
from pythonfw.functions import chinese_remainder

def preprocessing(data):
    values    = list(int(item) for item in findall(r'[0-9]+', data))
    equations = set()
    while values:
        ta, _, tn, d = values.pop(), values.pop(), values.pop(), values.pop()
        equations.add((-(ta + d), tn))
    return equations

def solver(equations):
    r, m = chinese_remainder(equations, get_modulo = True)
    yield r
    yield chinese_remainder({(r, m), (-7, 11)})
