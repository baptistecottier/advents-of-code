from collections import defaultdict


def parser(input_):
    replacements = defaultdict(list)
    text_replacements, molecule = input_.split('\n\n')
    for replacement in text_replacements.splitlines():
        start, end = replacement.split(" => ")
        replacements[start].append(end)
    return replacements, molecule

def solver(data):
    replacements, molecule = data
    candidates = set()
    
    for mol in replacements.keys():
        pieces = molecule.split(mol)
        for replacement in replacements[mol]:
            for index in range(1, 1 + molecule.count(mol)):
                candidates.add(mol.join(pieces[:index]) + replacement + mol.join(pieces[index:]))
                
    yield len(candidates)


    _, molecule = data
    a = len([c for c in molecule if c.isupper()])
    b = molecule.count('Rn') + molecule.count('Ar')
    c = molecule.count('Y')
    yield a - b - 2 * c - 1
