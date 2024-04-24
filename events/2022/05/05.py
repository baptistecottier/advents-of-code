from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input): 
    cargo, moves = puzzle_input.split('\n\n')
    moves  = extract_chunks(moves, 3)
    floors = cargo.splitlines()[::-1]
    width  = len(floors[0].replace(' ', ''))
    cargo  = ["" for _ in range(width)]
    
    for floor in floors[1:]: 
        crates = floor.split('[')
        pos    = len(crates[0]) // 4
        for crate in crates[1:]:
            cargo[pos] += crate[0]
            pos       += 1 + (crate.count(' ') // 4)
    return cargo, moves


def solver(cargo , moves):
    cargos = {-1: list(cargo), 1: list(cargo)}
    for qty, src, dst in moves:
        for version, cargo in cargos.items():
            cargo[dst - 1] += cargo[src - 1][-qty:][::version]
            cargo[src - 1] =  cargo[src - 1][:-qty]

    for cargo in cargos.values():
        yield ''.join([stack[-1] for stack in cargo])