from collections import defaultdict

def generator(input):
    replacements = defaultdict(list)
    text_replacements, molecule = input.split('\n\n')
    for replacement in text_replacements.splitlines():
        start, end = replacement.split(" => ")
        replacements[start].append(end)
    return replacements, molecule

def part_1(data): 
    candidates = set()
    replacements, molecule = data
    for mol in replacements.keys():
        pieces = molecule.split(mol)
        for replacement in replacements[mol]:
            for index in range(1, 1 + molecule.count(mol)):
                candidates.add(mol.join(pieces[:index]) + replacement + mol.join(pieces[index:]))
    return len(candidates)

def part_2(data):
    '''
    https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    '''
    _, molecule = data
    a = len([c for c in molecule if c.isupper()])
    b = molecule.count('Rn') + molecule.count('Ar')
    c = molecule.count('Y')
    return a - b - 2 * c - 1
