from parse import parse

class Group:
    def __init__(self, size, hp, weak, immune, attack_type, damage, initiative) -> None:
        self.size = size
        self.hp = hp
        self.weak = weak
        self.immune = immune
        self.attack_type = attack_type
        self.damage = damage
        self.initiative = initiative
    def __lt__(self, other):
        return self.size * self.damage < other.size * other.damage

def preprocessing(input_):
    system = []
    infection =  []
    for i, army in enumerate(input_.split('\n\n')):
        for grp in army.splitlines()[1:]:
            weak = set()
            immune = set()
            size, hp, specs, damage, attack_type, initiative = parse("{:d} units each with {:d} hit points{}with an attack that does {:d} {} damage at initiative {:d}", grp)
            if specs != ' ':
                for spec in specs[2:-2].split('; '):
                    if spec.startswith('weak'): 
                        spec = spec.replace('weak to ', '')
                        for s in spec.split(', '): weak.add(s)
                    if spec.startswith('immune'): 
                        spec = spec.replace('immune to ', '')
                        for s in spec.split(', '): immune.add(s)
            if i == 0: system.append(Group(size, hp, weak, immune, attack_type, damage, initiative))
            else: infection.append(Group(size, hp, weak, immune, attack_type, damage, initiative))
    return sorted(system, reverse = True), sorted(infection, reverse = True)

def solver(system, infection):
    for grp in system: print(grp.size * grp.damage)
    while system and infection:
        sys_target = []
        for grp in system:
            tgt = -1
            dmg = 0
            sze = 0
            typ = grp.attack_type
            for i, inf in enumerate(infection):
                if i in sys_target: continue
                if typ in inf.weak: inf_dmg = 2 * grp.damage
                elif typ in inf.immune: inf_dmg = 0
                else: inf_dmg = grp.damage
                
                if inf_dmg > dmg: 
                    dmg = inf_dmg
                    tgt = i
                elif inf_dmg == dmg: 
                    if inf.size > sze: 
                        sze = inf.size
                        tgt = i
                sys_target.append(i)
                     
    yield None