def preprocessing(input_):
    return (eval(sf) for sf in input_.splitlines())

def add(sf1, sf2):
    return [sf1, sf2]

def explode(sf):
    return