from parse import parse

def parser(input): 
    return [list(parse('{:l} {:l} {:d} if {:l} {}', instruction)) for instruction in input.splitlines()]

def solver(instructions):
    max_reg   = 0
    variables = {v[0]: 0 for v in instructions}
    for a, b, c, d, e in instructions:
        if eval(f"{variables[d]}{e}"): 
            variables[a] += c if (b == 'inc') else -c
            max_reg = max(max_reg, variables[a])

    yield max(variables.values())
    yield max_reg
    