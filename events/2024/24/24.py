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


def solver(wires: dict, connections):
    yield (compute(wires, connections))
    yield manual_debug(wires, connections, explanations = False)
    
    
def compute(wires, connections):
    while None in wires.values():
        for a, b, c, f in connections:
            if all(wires[w] != None for w in (a, b)):
                wires[c] = f(wires, a, b)
    s = ""
    for k, v in sorted(wires.items()):
        if k.startswith('z'):
            s = str(v) + s
    z = int(s, 2)
    return z

def manual_debug(wires, connections, explanations):
    """ Explanations for the manual solve of part 2.
    
    First print the binary value of x + y and z and look for the first different bit:"""
    if explanations:
        display_x_plus_y_and_z(wires, connections)
        """
        0b1000011000101111111110101011110010010001110000
        0b1000011001000000000000101011101110000001110000
                                            ↑
                            First different bit at index 10
        Let' see how z10 is computed:
                            mvs AND jvj -> z10
        and compare it to computations of z09, z08, etc.
                            nvv XOR (y09 XOR x09) -> z09
                            (x08 XOR y08) XOR fhf -> z08
        We can guess z10 is supposed to be computed as 
                            (x10 XOR y10) XOR ??? -> z10
        We have y10 XOR x10 -> jvj and jvj XOR mvs -> mkk, so:
                            (y10 XOR x10) XOR mvs -> mkk
        Swapping z10 with mkk seems relevant:"""
        connections = swap_connections(connections, 'z10', 'mkk')
        
        print("\nAfter first swap")
        display_x_plus_y_and_z(wires, connections)
        
        """
        0b1000011000101111111110101011110010010001110000
        0b1000011001000000000000101011101110010001110000
                                         ↑
                            First different bit at index 14
        z14 is computed as vjh OR fhq -> z14 and applying the same logic as above, 
        we have:
                            ndm XOR (x14 XOR y14) -> qbw
        Hence we swap qbw with z14."""
        connections = swap_connections(connections, 'z14', 'qbw')
        
        print("\nAfter second swap")
        display_x_plus_y_and_z(wires, connections)
        """
        0b1000011000101111111110101011110010010001110000
        0b1000011001000000000000101011110010010001110000
                              ↑
        First different bit at index 25. A lot of following values are also 
        different hence we can deduce the carry is wrong here.
        (y24 XOR x24) XOR ((bfq AND bjc) OR rgp) -> z24
        (x25 AND y25) XOR ((x24 AND y24) OR mcr) -> z25
        Left operand should be (x25 XOR y25). We have 
                x25 XOR y25 -> wjb and x25 AND y25 -> cvp
        so we swap wjb with cvp."""
        connections = swap_connections(connections, 'wjb', 'cvp')
        
        print("\nAfter third swap")
        display_x_plus_y_and_z(wires, connections)
        """
        0b111000100101111101010100000111011010111001100
        0b111000100011111101010100000111011010111001100
                    ↑
        First different bit at index 34
        We have x + y = z but that does not mean the problem is solved as we know 
        there are four swaps. To find the last one, we have to modify the values of x
        or y.
        
        """
        print("\nUsing random x and y")
        display_x_plus_y_and_z(wires, connections, randxy = True)
        """
        0b111000100101111101010100000111011010111001100
        0b111000100011111101010100000111011010111001100
        z34 is computed as y34 AND x34 -> z34 and applying the same logic as in the 
        two first cases, we have:
                            (y34 XOR x34) XOR mdh -> wcb.
        Hence, wcb should be z34 and we swap those values."""
        connections = swap_connections(connections, 'z34', 'wcb')
        
        print("\nAfter fourth swap")
        display_x_plus_y_and_z(wires, connections)
        """
        0b1100000111110010101001111011100100100101011110
        0b1100000111110010101001111011100100100101011110
        
        Let's check using randoms x and y:
        """
        display_x_plus_y_and_z(wires, connections, randxy = True)
        """
        0b1100110100100000100000101110000111110100000100
        0b1100110100100000100000101110000111110100000100
        """
        display_x_plus_y_and_z(wires, connections, randxy = True)
        """
        0b1011001001011100110001101100111010011011010111
        0b1011001001011100110001101100111010011011010111
        """
        display_x_plus_y_and_z(wires, connections, randxy = True)
        """
        0b11101100111001111111101101110011111001111010
        0b11101100111001111111101101110011111001111010
        
        Everything seems fixed, the four swaps are:
        - z10 with mkk
        - z14 with qbw
        - wjb with cvp
        - z34 with wcb
        
        Sorting them alphabetically results in cvp,mkk,qbw,wcb,wjb,z10,z14,z34
        """
    return "cvp,mkk,qbw,wcb,wjb,z10,z14,z34"

def swap_connections(connections, swap1, swap2):
    new_connections = []
    for (a, b, c, f) in connections:
        if c == swap1:
            c = swap2
        elif c == swap2:
            c = swap1
        new_connections.append((a, b, c, f))
    return new_connections
        
from random import random
def display_x_plus_y_and_z(wires, connections, randxy = False):
    x, y = "", ""
    for k, v in sorted(wires.items(), reverse=True):
        if k.startswith('x'): 
            if randxy:
                v = round(random())
                wires[k] = v
            x += str(v)
        if k.startswith('y'):
            if randxy:
                v = round(random())
                wires[k] = v
            y += str(v)
    x, y = int(x, 2), int(y, 2)
    print(f"x + y = {bin(y + x)}")
    print(f"    z = {bin(compute(wires, connections))}")