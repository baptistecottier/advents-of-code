
def preprocessing(input_): 
    reactions = {}
    for reaction in input_.splitlines():
        react_in, react_out = reaction.split(' => ')
        (a, b) = react_out.split(' ')
        react_out = (chem.split(' ') for chem in react_in.split(', '))
        chemicals = {}
        for d, e in react_out:
            chemicals[e] = int(d)
        reactions[b] = (int(a), chemicals)
    return reactions
from collections import defaultdict

def solver(reactions):
    def ore_quantity(chemical):
        if chemical == 'ORE': 
            return 1
        else:
            return sum(n * ore_quantity(chem) / reactions[chemical][0] for chem, n in reactions[chemical][1].items())
    yield sum(n * ore_quantity(chem) / reactions["FUEL"][0] for chem, n in reactions["FUEL"][1].items())

#178154