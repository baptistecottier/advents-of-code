def preprocessing(puzzle_input):
    inits, ops = puzzle_input.split('\n\n')
    wires = {}
    connections = []
    for init in inits.splitlines():
        w, v = init.split(': ')
        wires[w] = int(v)   
    for op in ops.splitlines():
        (a, o, b, _, c) = op.split(' ')
        wires[c] = None
        match o:
            case 'AND': connections.append((a, b, c, lambda w, x, y: w[x] and w[y]))
            case 'XOR': connections.append((a, b, c, lambda w, x, y: w[x] ^ w[y]))
            case 'OR': connections.append((a, b, c, lambda w, x, y: w[x] or w[y]))
    return wires, connections


def solver(wires, connections):
    ix = ""
    iy = ""

    for k, v in sorted(wires.items()):
        if k.startswith('x'):
            ix += str(v)
        if k.startswith('y'):
            iy += str(v)
    ix = int(ix[::-1], 2)
    iy = int(iy[::-1], 2)
    z = compute(wires, connections)
    yield z 
    yield "cvp,mkk,qbw,wcb,wjb,z10,z14,z34"
    
def compute(wires, connections):
    while None in wires.values():
        for a, b, c, f in connections:
            if all(wires[w] != None for w in (a, b)):
                wires[c] = f(wires, a, b)
            # print(c)
    s = ""
    for k, v in sorted(wires.items()):
        if k.startswith('z'):
            s += str(v)
    z = int(s[::-1], 2)
    return z

###     All what appears below are traces of what has been used to solve part 2    ###
    # print(str(bin(ix)))
    # print(str(bin(iy)))
    # print(str(bin(iy + ix)))
    # print(str(bin(z)))
    # z11, 
# mkk, z10, z14, qbw, 
# 
# cvp, wjb, z34, mpd
# cvp,mkk,mpd,qbw,wcb,z10,z14,z34
# 0b100001100010111111111 0101011110010010001110000
# 0b100001100100000000000 0101011110010010001110000

# 0b100001001110 1000100010011001101001100100101001
# 0b100001001101 1000100010011001101001100100101001


# kvd good

"""
(x25 AND y25) XOR (jfm OR mcr) -> z25

cvp XOR fqv -> z25

x25 AND y25 -> cvp
jfm OR mcr -> fqv
"""


# 0b111101100010111011101100110010110011011010101
# 0b111101100100111011101100110010110011011010101


"z10 mkk"

"""
vjh OR fhq -> z14
x14 XOR y14 -> tsp
cvp
wjb
nvv XOR kvd -> z09
y09 XOR x09 -> kvd
dkk OR tqj -> nvv

mvs AND jvj -> z10

((((x07 AND y07) OR ((07 XOR x07) AND tvn)) AND (x08 XOR y08)) OR (y08 AND x08)) XOR (y09 XOR x09) -> z09

y09 XOR x09 -> kvd

dkk OR tqj -> nvv
fhf AND btf -> dkk
y08 AND x08 -> tqj

y10 XOR x10 -> jvj


((x09 AND y09) OR (nvv AND (y09 XOR x09))) AND (y10 XOR x10) -> z10

y10 XOR x10 -> jvj

mqk OR vbs -> mvs
nvv AND kvd -> vbs
dkk OR tqj -> nvv

y09 XOR x09 -> kvd
x09 AND y09 -> mqk
z34, 
0b11110110001 0111011101100110010110011011010101
0b11110110010 0111011101100110010110011011010101

"""