def preprocessing(input_): 
    return [line.split() for line in input_.splitlines()]

def solver(program):
    fibo = int(program[2][1])
    fa   = int(program[16][1])
    fb   = int(program[17][1])
    a, b = 1, 1

    for f in range(fibo + 8): 
        a, b = b, a + b
        if f == fibo: yield a + fa * fb
    yield a + fa * fb
