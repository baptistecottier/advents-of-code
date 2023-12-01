def preprocessing(file):
    return list(int(x) for x in file.splitlines())

def solver(changes): 
    yield sum(changes)
    frequencies = set()
    frequency   = 0
    index       = 0
    while frequency not in frequencies:
        frequencies.add(frequency)
        frequency += changes[index]
        index = (index + 1) % len(changes)
    yield frequency