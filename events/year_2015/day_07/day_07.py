"""Advent of Code - Year 2015 - Day 07"""

from dataclasses import dataclass
from operator import and_, lshift, or_, rshift, inv
from typing import Optional, Callable
from pythonfw.classes import Register


@dataclass
class Gate:
    """A class representing a logical gate in a circuit.

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
    """Converts circuit instructions into a list of Gate objects.

    Args:
        puzzle_input (str): String containing circuit gate instructions

    Returns:
        list[Gate]: List of Gate objects representing the circuit
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


def solver(circuit: list[Gate], wire: Optional[str] = None):
    """Solves the circuit by evaluating gates and calculating wire signals.

    Args:
        circuit (list[Gate]): List of Gate objects representing the circuit's 
            connections and operations
        wire (str, optional): The target wire to evaluate. If None, evaluates 
            the whole circuit. Defaults to None.

    Yields:
        int: Signal values:
            - First yield: The initial signal on wire 'a'
            - Second yield: The signal on wire 'a' after setting wire 'b' to 
              the initial signal
    """
    if not wire:
        circuit.sort(key = lambda gate: (len(gate.wire_out) , gate.wire_out))
        circuit = circuit[1:] + [circuit[0]]

    def run(circuit):
        wires = Register()
        for gate in circuit:
            wires[gate.wire_out] = gate.op(*(wires.get(a) for a in gate.wire_in))
        return wires['a'] % pow(2,16)

    signal = run(circuit)
    yield signal

    circuit[0] = Gate(lambda x: x, 'b', (str(signal),))
    yield run(circuit)
