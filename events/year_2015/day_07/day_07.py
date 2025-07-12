"""Advent of Code - Year 2015 - Day 07"""

# Standard imports
from collections.abc  import Callable
from dataclasses      import dataclass
from operator         import and_, inv, lshift, or_, rshift

# First-party import
from pythonfw.classes import Register


@dataclass
class Gate:
    """
    A class representing a logical gate in a circuit.

    This class defines a gate that performs operations on input wires and outputs
    the result to an output wire.

    Attributes:
        op (callable): The operation function to be performed by the gate.
        wire_out (str): The identifier of the output wire.
        wire_in (tuple[str]): A tuple containing the identifiers of input wires.
    """
    op: Callable
    wire_out: str
    wire_in: tuple[str, ...]


def preprocessing(puzzle_input: str) -> list[Gate]:
    """
    Converts circuit instructions into a list of Gate objects.

    Args:
        puzzle_input (str): String containing circuit gate instructions

    Returns:
        list[Gate]: List of Gate objects representing the circuit
        
    Examples:
        >>> preprocessing("123 -> x")
        [Gate(op=<function <lambda> at ...>, wire_out='x', wire_in=('123',))]
        
        >>> preprocessing("NOT x -> h")
        [Gate(op=<function inv at ...>, wire_out='h', wire_in=('x',))]
        
        >>> preprocessing("x AND y -> z")
        [Gate(op=<function and_ at ...>, wire_out='z', wire_in=('x', 'y'))]
    """
    circuit = []
    for gate in puzzle_input.splitlines():
        in_, out_ = gate.split(' -> ')
        data = in_.split(' ')
        if len(data) == 1:
            circuit.append(Gate(lambda x: x, out_, (data[0],)))
        elif len(data) == 2:
            circuit.append(Gate(inv, out_, (data[1],)))
        else:
            w1, op, w2 = data
            match op:
                case 'AND': op = and_
                case 'OR' : op = or_
                case 'RSHIFT': op = rshift
                case 'LSHIFT': op = lshift
                case _: raise ValueError(f"Invalid function name: {op}")
            circuit.append(Gate(op, out_, (w1, w2)))
    return circuit


def solver(circuit: list[Gate], wire: str = "a") -> tuple[int, int]:
    """
    Solves a circuit puzzle by finding signal values for a specific wire.
    
    Args:
        circuit: List of Gate objects representing the circuit
        wire: Wire identifier to find the signal for (default: "a")
        
    Returns:
        Tuple of (initial_signal, modified_signal) where modified_signal
        is the result after setting wire 'b' to the initial signal value
        
    Examples:
        >>> gates = [Gate(lambda: 123, 'x', ()), Gate(lambda x: x, 'a', ('x',))]
        >>> solver(gates)
        (123, 123)
    """
    if wire == "a":
        circuit.sort(key = lambda gate: (len(gate.wire_out) , gate.wire_out))
        circuit = circuit[1:] + [circuit[0]]

    def run(circuit):
        wires = Register()
        for gate in circuit:
            wires[gate.wire_out] = gate.op(*(wires.get(a) for a in gate.wire_in))
        return wires['a'] % pow(2,16)

    signal = run(circuit)
    circuit[0] = Gate(lambda x: x, 'b', (str(signal),))

    return signal, run(circuit)
