"""
Advent of Code - Year 2019 - Day 14
https://adventofcode.com/2019/day/14
"""

# Standard imports
from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Reaction:
    """
    Represents a reaction producing out_qty units of a chemical from a list of
    (input_name, input_qty) pairs.
    """
    out_qty: int
    inputs: list[tuple[str, int]]


def preprocessing(puzzle_input: str) -> dict[str, Reaction]:
    """
    Parses the puzzle input string and returns a dictionary mapping each output chemical name to
    the Reaction producing it.
    """
    reactions = {}
    puzzle_input = puzzle_input.replace(' =>', '').replace(',', '')
    for reaction in puzzle_input.splitlines():
        details = reaction.split(' ')
        inputs = [(details[i], int(details[i - 1])) for i in range(1, len(details) - 2, 2)]
        reactions[details[-1]] = Reaction(int(details[-2]), inputs)
    return reactions


def solver(reactions: dict[str, Reaction]) -> Iterator[int]:
    """
    Yields the ORE needed to produce 1 FUEL, then the maximum amount of FUEL that can be produced
    with one trillion ORE, found by binary search.
    """
    levels = topologic_sort(reactions.copy())
    ore_for_1_fuel = ore_needed(1, reactions, levels)
    yield ore_for_1_fuel

    units = 1_000_000_000_000
    low = units // ore_for_1_fuel
    high = units + 1
    while high > low + 1:
        k = (low + high) // 2
        ore = ore_needed(k, reactions, levels)
        if ore > units:
            high = k
        else:
            low = k
    yield low


def ore_needed(k: int, reactions: dict[str, Reaction], levels: dict[str, int]) -> int:
    """
    Computes the ORE needed to produce k FUEL by expanding chemicals from the highest level down,
    so that each chemical's total demand is known before rounding it up to whole reactions.
    """
    needed = {name: 0 for name in reactions.keys()}
    needed['FUEL'] = k
    needed['ORE'] = 0

    order = sorted(reactions, key=levels.get, reverse=True)
    for name in order:
        coeff = 1 + ((needed[name] - 1) // reactions[name].out_qty)
        for n, q in reactions[name].inputs:
            needed[n] += coeff * q
    return needed['ORE']


def topologic_sort(reactions: dict[str, Reaction]) -> dict[str, int]:
    """
    Assigns each chemical a level equal to 1 + the maximum level of its inputs, ORE being level 0.
    Empties the given dictionary, so a copy should be passed.
    """
    placed = {'ORE'}
    levels = {'ORE': 0}
    level = 1
    newly_placed = set()
    while reactions:
        updated = False
        for name, reaction in reactions.items():
            inputs = reaction.inputs
            if all(n in placed for n, _ in inputs):
                newly_placed.add(name)
                levels[name] = level
                updated = True
                del reactions[name]
                break
        if not updated:
            placed.update(newly_placed)
            level += 1
            newly_placed.clear()
    return levels
