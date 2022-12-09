def generator(input) : 
    circuit = [gate.rsplit(' ', 1) for gate in input.splitlines()]
    circuit.sort(key=lambda c : (len(c[1]) , c[1]))
    return circuit

def part_1(input) : 
    return solver(input, 0)
    
def part_2(input) : 
    return solver(input, solver(input, 0))


def mymap(input, dict) :
    if input in dict :  
        return dict[input] 
    else : 
        return int(input)

def solver(circuit, b) :
    wires = {"b" : b}
    for [input, out] in circuit[2-(b==0):]+[circuit[0]] :
        [in1, in2, in3] = (input.split(' ')+[0])[:3]
        match in2 :
            case "AND" : wires[out] = mymap(in1, wires) & mymap(in3, wires) 
            case "OR" : wires[out] = mymap(in1, wires) | mymap(in3, wires)
            case "RSHIFT" : wires[out] = wires[in1] >> int(in3)
            case "LSHIFT" : wires[out] = wires[in1] << int(in3)
            case "->" :wires[out] = mymap(in1, wires)
            case _ : wires[out] = ~ mymap(in2, wires)
    return wires["a"]
