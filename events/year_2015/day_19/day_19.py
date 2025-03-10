"""Advent of Code - Year 2015 - Day 19"""

from collections import defaultdict


def preprocessing(puzzle_input: str) -> tuple[defaultdict[list], str]:
    """
    Preprocess the puzzle input into a dictionary of replacements and a molecule.

    Args:
        puzzle_input (str): The puzzle input containing replacements and a molecule.

    Returns:
        tuple: A tuple containing:
            - defaultdict[list]: Dictionary mapping input strings to lists of possible replacements.
            - str: The molecule to transform.
    """
    replacements = defaultdict(list)
    text_replacements, molecule = puzzle_input.split('\n\n')
    for replacement in text_replacements.splitlines():
        start, end = replacement.split(" => ")
        replacements[start].append(end)
    return replacements, molecule


def solver(replacements: defaultdict[list], molecule_: str):
    """
    Solve the molecule replacement problem.
    
    Args:
        replacements: Dictionary of molecule parts to their possible replacements
        molecule_: The target molecule string
    
    Yields:
        int: First, the number of distinct molecules that can be created with one replacement
        int: Second, the minimum number of steps to create the target molecule
        
    Note:
        See https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/ for part 2
        explanation.
    """
    candidates = set()
    molecule = molecule_
    for mol in replacements.keys():
        pieces = molecule.split(mol)
        for replacement in replacements[mol]:
            for index in range(1, 1 + molecule.count(mol)):
                candidates.add(mol.join(pieces[:index]) + replacement + mol.join(pieces[index:]))
    yield len(candidates)

    a = len([c for c in molecule_ if c.isupper()])
    b = molecule_.count('Rn') + molecule_.count('Ar')
    c = molecule_.count('Y')
    yield a - b - 2 * c - 1
