from aoctools import Register

def parser(input): 
    circuit = [gate.rsplit(' ', 1) for gate in input.splitlines()]
    circuit.sort(key=lambda c: (len(c[1]) , c[1]))
    b = circuit[1][0].split(' ')
    return circuit[2:] + [circuit[0]], int(b[0])

        
def solver(circuit_infos):
    circuit, b = circuit_infos
    
    def run_circuit(b):
        wires = Register({'b': b})
        for (input, out) in circuit:
            [in1, in2, in3] = (input.split(' ') + [0])[:3]
            match in2:
                case "AND"      : wires[out] = wires.get(in1) & wires.get(in3) 
                case "OR"       : wires[out] = wires.get(in1) | wires.get(in3)
                case "RSHIFT"   : wires[out] = wires[in1] >> int(in3)
                case "LSHIFT"   : wires[out] = wires[in1] << int(in3)
                case "->"       : wires[out] = wires.get(in1)
                case _          : wires[out] = ~ wires.get(in2)
        return wires["a"]

    signal = run_circuit(b)
    yield signal
    yield run_circuit(signal)

    
