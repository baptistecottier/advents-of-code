from pythonfw.classes import Register
from operator         import and_, lshift, or_, rshift, inv
from copy             import deepcopy


def preprocessing(input_): 
    circuit = []
    
    for gate in input_.splitlines():
        in_, out_ = gate.split(' -> ')
        data = in_.split(' ')
        if len(data) == 1:   circuit.append((out_, lambda x: x, data[0]))
        elif len(data) == 2: circuit.append((out_, inv, data[1]))
        else: 
            w1, op, w2 = data
            match op:
                case 'AND': f = and_
                case 'OR' : f = or_
                case 'RSHIFT': f = rshift
                case 'LSHIFT': f = lshift
            circuit.append((out_, f, w1, w2))
    return circuit
    


def solver(circuit, wire = None):
    if not wire:
        circuit.sort(key = lambda c: (len(c[0]) , c[0]))
        circuit = circuit[1:] + [circuit[0]]
        
    def run(circuit):
        wires = Register()
        for out_, f, *args in circuit:
            wires[out_] = f(*(wires.get(a) for a in args))
        return wires['a'] % pow(2,16)
        
    signal = run(circuit)
    yield signal
    
    circuit[0] = ('b', lambda x: x, str(signal))
    yield run(circuit)

    
