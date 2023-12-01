from pythonfw.classes import Particule
from pythonfw.functions import extract_chunks

def preprocessing(input_): 
    return [Particule(*particule) for particule in extract_chunks(input_, 9)]

def solver(particules):
    yield min(range(len(particules)), key = lambda i: particules[i])

    for j in range(50):
        for particule in particules:
            particule.v.move(*particule.a.xyz())
            particule.p.move(*particule.v.xyz())
        positions = list(particule.p.xyz() for particule in particules)
        positions = set(item for item in positions if positions.count(item) > 1)
        particules = list(item for item in particules if item.p.xyz() not in positions)
    yield len(particules)