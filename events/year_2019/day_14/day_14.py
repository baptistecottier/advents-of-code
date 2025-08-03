"""
Advent of Code - Year 2019 - Day 14
https://adventofcode.com/2019/day/14
"""

from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Chemical:
    """
    Represents a chemical with a name and a quantity.
    """
    name: str
    qty: int


def preprocessing(puzzle_input):
    """
    Parses the puzzle input string and returns a dictionary mapping output Chemical objects to
    lists of input Chemical objects representing the reactions.
    """
    puzzle_input = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""
    reactions = {}
    puzzle_input = puzzle_input.replace(' =>', '').replace(',', '')
    for reaction in puzzle_input.splitlines():
        details = reaction.split(' ')
        chem_out = Chemical(details.pop(), int(details.pop()))
        chem_in = []
        while details:
            chem_in.append(Chemical(details.pop(), int(details.pop())))
        reactions[chem_out] = chem_in
    return reactions


def solver(reactions):
    """
    Processes a set of chemical reactions to break down 'FUEL' into its base components, ultimately
    reducing all chemicals to 'ORE'.
    """
    fuel = Chemical(name='FUEL', qty=1)
    while any(c.name != 'ORE' for c in reactions[fuel]):
        for _ in range(len(reactions[fuel])):
            chem = reactions[fuel].pop(0)
            if chem.name == 'ORE':
                reactions[fuel].append(chem)
            else:
                for c in reactions[chem]:
                    reactions[fuel].append(Chemical(c.name, chem.qty * c.qty))
    print(reactions)
