from parse import parse

def generator(input): return input.splitlines()
    
def part_1(input): return solver(input, 1)
    
def part_2(input): return solver(input, 8)
    
def solver(input, delta):
    fibo = parse('cpy {:d} d',input[2])[0] # Retrieve 26
    fa = parse('cpy {:d} c', input[16])[0] # Retrieve 13 
    fb = parse('cpy {:d} d', input[17])[0] # Retrieve 14
    a , b = 1 , 1

    for _ in range(fibo + delta) : a , b = b , a + b
       
    return a + fa * fb
