def generator(input): 
    circuit = [gate.rsplit(' ', 1) for gate in input.splitlines()]
    circuit.sort(key=lambda c: (len(c[1]) , c[1]))
    b = circuit[1][0].split(' ')
    return circuit[2:] + [circuit[0]], int(b[0])

def part_1(circuit_infos):
    circuit, b = circuit_infos 
    return run_circuit(circuit, b)
    
def part_2(circuit_infos): 
    circuit, b = circuit_infos 
    return run_circuit(circuit, run_circuit(circuit, b))


def mymap(entry, dict):
    if entry in dict:  
        return dict[entry] 
    else: 
        return int(entry)

def run_circuit(circuit, b):
    wires = {"b": b}
    for (input, out) in circuit:
        [in1, in2, in3] = (input.split(' ') + [0])[:3]
        match in2:
            case "AND"      : wires[out] = mymap(in1, wires) & mymap(in3, wires) 
            case "OR"       : wires[out] = mymap(in1, wires) | mymap(in3, wires)
            case "RSHIFT"   : wires[out] = wires[in1] >> int(in3)
            case "LSHIFT"   : wires[out] = wires[in1] << int(in3)
            case "->"       : wires[out] = mymap(in1, wires)
            case _          : wires[out] = ~ mymap(in2, wires)
    return wires["a"]
