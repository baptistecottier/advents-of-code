"""
Advent of Code - Year 2021 - Day 14
https://adventofcode.com/2021/day/14
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> tuple[dict[str, int], str, dict[str, str]]:
    """
    Parses the puzzle input into a dictionary of pair counts, the last character of the template,
    and a dictionary of insertion rules.
    """
    template, insertions = puzzle_input.split('\n\n')
    insertions = dict([insertion.split(' -> ') for insertion in insertions.splitlines()])
    return {pair: template.count(pair) for pair in insertions.keys()}, template[-1], insertions


def solver(molecule: dict[str, int], last: str, insertions: dict[str, str]) -> Iterator[int]:
    """
    Simulates polymerization steps and yields the difference between the most and least common
    elements after specified rounds.
    """
    for r in range(40):
        if r == 10:
            counter = {atom: sum(molecule[pair] for pair in molecule.keys() if atom == pair[0])
                       for atom in set(insertions.values())}
            counter[last] += 1
            yield sorted(counter.values())[-1] - sorted(counter.values())[0]

        new_molecule = {pair: 0 for pair in insertions.keys()}
        for pair in molecule.keys():
            new_molecule[pair[0] + insertions[pair]] += molecule[pair]
            new_molecule[insertions[pair] + pair[1]] += molecule[pair]
        molecule = new_molecule

    counter = {atom: sum(molecule[pair] for pair in molecule.keys() if atom == pair[0])
               for atom in set(insertions.values())}
    counter[last] += 1

    yield sorted(counter.values())[-1] - sorted(counter.values())[0]
