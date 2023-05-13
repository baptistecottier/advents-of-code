def generator(input):
    orbits = {}
    for orbit in input.splitlines():
        ctr, pnt = orbit.split(')')
        orbits[pnt] = ctr
    return orbits

def part_1(input):
    paths = map_orbits(input)
    total_orbits = 0
    for planet in input.keys():
        for path in paths:
            if planet in path:
                total_orbits += path.index(planet)
                break
    return total_orbits
    
def part_2(input):
    paths = map_orbits(input)
    for path in paths: 
        if 'YOU' in path: 
            for dst in paths:
                if 'SAN' in dst:
                    for p in path[::-1]:
                        if p in dst:
                            return path.index('YOU') - path.index(p) + dst.index('SAN') - dst.index(p) - 2


def map_orbits(input):
    paths = []
    for p in [ends for ends in input.keys() if ends not in input.values()]: 
        path = [p]
        src = input[p]
        while src != 'COM':
            path.append(src)
            src = input[src]
        path.append('COM')
        paths.append(path[::-1])
    return paths