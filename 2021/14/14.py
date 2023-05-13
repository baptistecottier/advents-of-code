def generator(input): 
    template, insertions = input.split('\n\n')
    insertions = {start : end for start, end in [insertion.split(' -> ') for insertion in insertions.splitlines()]}
    template = ({pair: template.count(pair) for pair in insertions.keys()}, template[-1])
    return template, insertions

def part_1(input): 
    (molecule, last), insertions = input
    return apply_insertions(molecule, insertions, last, 10)
    
def part_2(input): 
    (molecule, last), insertions = input
    return apply_insertions(molecule, insertions, last, 40)
 

def apply_insertions(molecule, insertions, last, rounds):
    for _ in range(rounds):
        new_molecule = {pair: 0 for pair in insertions.keys()}
        for pair in molecule.keys(): 
            new_molecule[pair[0] + insertions[pair]] += molecule[pair]
            new_molecule[insertions[pair] + pair[1]] += molecule[pair]
        molecule = new_molecule
    counter = {atom: sum(molecule[pair] for pair in molecule.keys() if atom == pair[0]) for atom in set(insertions.values())}
    counter[last] += 1
    return sorted(counter.values())[-1] - sorted(counter.values())[0]
