def preprocessing(puzzle_input):
    return (eval(sf) for sf in puzzle_input.splitlines())

def add(sf1, sf2):
    return [sf1, sf2]

def explode(sf):
    return