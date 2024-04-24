def preprocessing(puzzle_input): 
    template, insertions = puzzle_input.split('\n\n')
    insertions = {start: end for start, end in [insertion.split(' -> ') for insertion in insertions.splitlines()]}
    return {pair: template.count(pair) for pair in insertions.keys()}, template[-1], insertions


def solver(molecule, last, insertions):
    for r in range(40):
        if r == 10: 
            counter = {atom: sum(molecule[pair] for pair in molecule.keys() if atom == pair[0]) for atom in set(insertions.values())}
            counter[last] += 1
            yield sorted(counter.values())[-1] - sorted(counter.values())[0]
        new_molecule = {pair: 0 for pair in insertions.keys()}
        for pair in molecule.keys(): 
            new_molecule[pair[0] + insertions[pair]] += molecule[pair]
            new_molecule[insertions[pair] + pair[1]] += molecule[pair]
        molecule = new_molecule
        
    counter = {atom: sum(molecule[pair] for pair in molecule.keys() if atom == pair[0]) for atom in set(insertions.values())}
    counter[last] += 1
    yield sorted(counter.values())[-1] - sorted(counter.values())[0]
