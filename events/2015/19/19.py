from collections import defaultdict


def preprocessing(input_):
    replacements = defaultdict(list)
    text_replacements, molecule = input_.split('\n\n')
    for replacement in text_replacements.splitlines():
        start, end = replacement.split(" => ")
        replacements[start].append(end)
    return replacements, molecule

def solver(replacements, molecule_):
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
