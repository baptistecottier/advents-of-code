from AoC_tools import read_input

diag = read_input().splitlines()
nb_bits=len(diag[0])
p1_diag = ''.join(diag)

gamma=int(''.join([max(['0','1'], key = lambda item : p1_diag[b::nb_bits].count(item)) for b in range(nb_bits)]),2)
print('The power consumption of the submarine is', (2**nb_bits-1-gamma)*gamma)


diag_cpy = diag.copy()
OGR , CSR = '' , ''

while len(diag_cpy)>1:
    mb=max(['1','0'], key = lambda item : [d[0] for d in diag_cpy].count(item))
    diag_cpy = [d[1:] for d in diag_cpy if d[0]==mb]
    OGR+=mb
OGR=int(OGR+diag_cpy[0],2)

while len(diag)>1:
    mb=min(['0','1'], key = lambda item : [d[0] for d in diag].count(item))
    diag = [d[1:] for d in diag if d[0]==mb]
    CSR+=mb
CSR = int(CSR+diag[0],2)

print('The life support rating of the submarine is', OGR*CSR)

