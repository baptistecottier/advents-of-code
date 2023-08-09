from itertools import pairwise, product
import re

def generator(input_):
    spacetime = set()
    coordinates = [int(item) for item in re.findall(r'-?[0-9]+', input_)]
    while coordinates:
        spacetime.add((coordinates.pop(), coordinates.pop(), coordinates.pop(), coordinates.pop()))
    return spacetime

def solver(input_):
    yield part_1(input_)

def part_1(spacetime):
    constellations = list()
    constellation = [spacetime.pop()]
    while spacetime:
        size = len(constellation)
        for pos in spacetime:
            if any(distance(cc, pos) <= 3 for cc in constellation): 
                constellation.append(pos)
                spacetime.remove(pos)
                break
        if len(constellation) == size:
            constellations.append(constellation)
            constellation = [spacetime.pop()]

    return len(constellations) + 1
    
            
                
        
def distance(a, b): 
    return sum(abs(x -  y) for x, y in zip(a, b))