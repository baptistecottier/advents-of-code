from itertools import product
from typing    import Generator


def preprocessing(input: str) -> dict[str: str]:
    orbits: dict[str: str] = {}
    for orbit in input.splitlines():
        ctr, pnt = orbit.split(')')
        orbits[pnt] = ctr
    return orbits


def solver(orbits: dict[str: str]) -> Generator:
    paths: list[list[str]] = map_orbits(orbits)
    total_orbits : int     = 0
    to_yield: bool         = True
    
    for planet in orbits.keys():
        for path in paths:
            if to_yield and 'YOU' in path: 
                for dst, p in product(paths, path[::-1]):
                    if {'SAN', p} <= set(dst):
                        yield (2, path.index('YOU') - path.index(p) + dst.index('SAN') - dst.index(p) - 2)
                        to_yield = False
                        break
            if planet in path:
                total_orbits += path.index(planet)
                break
    yield (1, total_orbits)


def map_orbits(orbits: dict[str: str]) -> list[list[str]]:
    paths: list[list[str]] = []
    for p in [ends for ends in orbits.keys() if ends not in orbits.values()]: 
       
        path: list[str] = [p]
        src: str        = orbits[p]
        while src != 'COM':
            path.append(src)
            src = orbits[src]
        path.append('COM')
        paths.append(path[::-1])

    return paths