from itertools import pairwise, product
from re        import findall
from pythonfw.functions import extract_chunks

def preprocessing(input_):
    return extract_chunks(input_, 4)

def solver(spacetime):
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

    yield len(constellations) + 1
    
        
def distance(a, b): 
    return sum(abs(x -  y) for x, y in zip(a, b))