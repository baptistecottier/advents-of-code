from pythonfw.classes   import Particule
from pythonfw.functions import sign
from re                 import findall
from itertools          import product


def preprocessing(puzzle_input):
     target = (int(n) for n in findall(r'[-]?[0-9]+', puzzle_input))
     return target

 
def solver(target):
    tx_min, tx_max, ty_min, ty_max = target

    global_max_y   = 0
    good_init_velo = 0

    for vx, vy in product(range(tx_max+1), range(ty_min, -ty_min)):
        pos = Particule(0, 0, 0, vx + sign(vx), vy + 1, 0, 0, -1, 0)
        max_y = 0
        while pos.p.x <= tx_max and pos.p.y >= ty_min:
            pos.move()
            pos.v.x -= sign(pos.v.x)
            max_y = max(max_y, pos.p.y)
            
            if (tx_min <= pos.p.x <= tx_max) and (ty_min <= pos.p.y <= ty_max):
                good_init_velo += 1
                global_max_y = max(global_max_y, max_y)
                break
            
    yield global_max_y
    yield good_init_velo
                  