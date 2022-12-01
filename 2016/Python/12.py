from parse import parse

with open("inputs/12.txt") as f:
    instructions=f.read().splitlines()

# After analysis, we do not need to execute the instructions given in input
# With F(n) denoting the n-th Fibonacci number, the solution is :
# F(26)+13*14 , F(26+9)+13*14
# where 26, 13, 14 are the only useful integer in the input

fibo = parse('cpy {:d} d',instructions[2])[0] # Retrieve 26
fa = parse('cpy {:d} c', instructions[16])[0] # Retrieve 13 
fb = parse('cpy {:d} d', instructions[17])[0] # Retrieve 14

# Compute successive Fibonacci numbers
a , b = 1 , 1
for i in range(fibo+8) :
    a , b = b , a + b
    if i==fibo : P1 = a # a is the fibo-th Fibonacci number

print('Without any particular setting, the value left in register a is',P1 + fa * fb)
print('However, with register c intialized at 1, the value left in register a is', a + fa * fb)

