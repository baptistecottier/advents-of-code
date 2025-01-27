from collections import deque
from dataclasses import dataclass, replace

@dataclass
class Unit:
    id: int
    x: int
    y: int
    type: str
    hp: int

    
def preprocessing(data):
    n_id = 0
    cave: set = set()
    units: list[Unit] = list()
    for y, line in enumerate(data.splitlines()):
        for x, char in enumerate(line):
            if char == '#':
                cave.add((x, y))
            elif char in 'EG':
                units.append(Unit(n_id, x, y, char, 200))
                n_id += 1
    return units, cave

def sorted_units(units):
    units = [u for u in units if u.hp > 0]
    return sorted(units, key = lambda u: (u.y, u.x))

from copy import deepcopy
def solver(units, cave):
    yield fight([replace(u) for u in units], cave)
    l = 3
    r = 200
    outcomes = {}
    while r - l > 1:
        elf_pa = (l + r) // 2
        outcome = fight([replace(u) for u in units], cave, no_elf_loss = True, elf_power_attack = elf_pa)
        if outcome == -1:
            l = elf_pa
        else: 
            outcomes[elf_pa] = outcome
            r = elf_pa

    yield outcomes[min(outcomes.keys())]
            

def fight(units, cave, no_elf_loss = False, elf_power_attack = 3):
    round = 0
    while count_units_types(units) == 2:
        # New round
        # Set the turns order
        units = sorted_units(units)      
        n_units = len(units)
        for i_unit in range(n_units):
            if i_unit == n_units - 1: round += 1
            unit = units[i_unit]
            if unit.hp < 0: 
                continue
            ux = unit.x
            uy = unit.y

            #Check in range of any adversary
            target = None
            for adv in units:
                if adv.type != unit.type and adv.hp > 0:
                    if (adv.x, adv.y) in {(ux, uy - 1), (ux - 1, uy), (ux + 1, uy), (ux, uy + 1)}:
                        if ((target == None) or
                            (adv.hp < target.hp) or 
                            (adv.hp == target.hp and (adv.y, adv.x) < (target.y, target.x))):
                            target = adv
            
            if target != None:
                if target.type == 'E':
                    target.hp -= 3
                else:
                    target.hp -= elf_power_attack
                if target.hp <= 0:
                    if target.type == 'E' and no_elf_loss: return -1
                    if count_units_types(units) == 1:
                        outcome = (round + (i_unit == n_units - 1)) * sum(max(0, u.hp) for u in units)
                        return outcome
                
            # If no unit in range move toward the closest one
            else:
                nearest = len(cave)
                nx, ny = (100, 100)
                for adv in units:
                    if adv.type != unit.type and adv.hp > 0:
                        ax = adv.x
                        ay = adv.y
                        for tx, ty in {(ax, ay - 1), (ax - 1, ay), (ax + 1, ay), (ax, ay + 1)}: # Checking all four sides of attack
                            reachable, dist, (mx, my) = is_reachable((ux, uy), (tx, ty), cave, {(u.x, u.y) for u in units if u.hp > 0})
                            if reachable:
                                if dist < nearest or (dist == nearest and (ty, tx) < (ny, nx)): 
                                    nearest = dist
                                    nx = mx
                                    ny = my
                if (nx, ny) != (100, 100):
                    units[i_unit].x = nx
                    units[i_unit].y = ny
                ux = nx
                uy = ny
                
                # Attack
                for adv in units:
                    if adv.type != unit.type and adv.hp > 0:
                        if (adv.x, adv.y) in {(ux, uy - 1), (ux - 1, uy), (ux + 1, uy), (ux, uy + 1)}:
                            if ((target == None) or
                                (adv.hp < target.hp) or 
                                (adv.hp == target.hp and (adv.y, adv.x) < (target.y, target.x))):
                                target = adv
                
                if target != None:
                    if target.type == 'E':
                        target.hp -= 3
                    else:
                        target.hp -= elf_power_attack
                    if target.hp <= 0:
                        if target.type == 'E' and no_elf_loss: return -1 
                        if count_units_types(units) == 1:
                            outcome = (round + (i_unit == n_units - 1)) * sum(u.hp for u in units)
                            return outcome
    

def count_units_types(units):
    return len(set({u.type for u in units if u.hp > 0}))

def is_reachable(start, end, cave, units):
    if end in cave: 
        return False, -1, start
    
    queue = deque([[start]])
    seen = set([start])
    
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return True, len(path) - 1, path[1]
        for x2, y2 in ((x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)):
            if (x2, y2) not in seen and (x2, y2) not in cave and (x2, y2) not in units:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return False, -1, start