from pythonfw.classes   import Particule
from pythonfw.functions import extract_chunks, screen_reader

def preprocessing(input):
    details = []
    particules = {Particule(px, py, 0, vx, vy, 0) for (px, py, vx, vy) in extract_chunks(input, 4)}
    return particules

def solver(particules):
    seconds = 0
    while True:
        seconds += 1
        for particule in particules:
            particule.p.move(*particule.v.xy())
        lst_y = {particule.p.y for particule in particules}
        min_y = min(lst_y)
        max_y = max(lst_y)
        if max_y - min_y < 10: 
            break
        
    positions = set(particule.p.xy() for particule in particules)
    yield screen_reader(positions)
    yield seconds
