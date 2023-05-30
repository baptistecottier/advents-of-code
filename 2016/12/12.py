def generator(input): 
    return [line.split() for line in input.splitlines()]
    
def part_1(program): 
    return execute(program, 1)
    
def part_2(program): 
    return execute(program, 8)
    
def execute(program, delta):
    fibo = int(program[2][1])
    fa   = int(program[16][1])
    fb   = int(program[17][1])
    a, b = 1, 1

    for _ in range(fibo + delta): 
        a, b = b, a + b
    return a + fa * fb
