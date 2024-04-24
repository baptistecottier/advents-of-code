import string 

def preprocessing(puzzle_input):
    return puzzle_input

def solver(polymer_):
    units            = list(zip(string.ascii_lowercase, string.ascii_uppercase))
    new_length       = 0 
    shortest_polymer = len(polymer_)
    
    for unit_low, unit_up in [('', '')] + units:
        polymer = polymer_.replace(unit_low, '').replace(unit_up, '')
        
        length = len(polymer)
        while length != new_length:
            length = len(polymer)
            for l, u in units:
                polymer = polymer.replace(l + u,'').replace(u + l,'')
            new_length = len(polymer)
        shortest_polymer = min(shortest_polymer, new_length)
        
        if unit_low == '' : yield shortest_polymer
    
    yield shortest_polymer