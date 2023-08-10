from pythonfw.functions import extract_chunks

def preprocessing(input): 
    [a, b] = input.split('\n\n')
    rearrangements = extract_chunks(b, 3)
    cargo_lines = a.splitlines()
    cargo_width = len(cargo_lines[-1].replace(' ',''))
    cargo = ["" for _ in range(cargo_width)]
    for c in cargo_lines[:-1]: 
        v = c.split('[')
        s = len(v[0]) // 4
        for cc in v[1:]:
            cargo[s] =  cc[0] + cargo[s]
            s += 1 + (cc.count(' ') // 4)
    return (cargo, rearrangements)


def solver(procedure): 
    (cargo , rearrangements) = procedure
    cargos = {-1: list(cargo), 1: list(cargo)}
    for (l, s, e) in rearrangements:
        for version, cargo in cargos.items():
            cargo[e - 1] += cargo[s - 1][-l:][::version]
            cargo[s - 1] =  cargo[s - 1][:-l]

    for cargo in cargos.values():
        yield ''.join([stack[-1] for stack in cargo])