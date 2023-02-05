import copy

def generator(specs) : 
    s=[]
    for spec in specs.splitlines() : 
        s.append(int(spec.split(': ')[1]))
    return s


def part_1(input) : 
    list_manas = []
    player_turn([], 50 , 500 , input[0], input[1] , 0 , False, list_manas)
    return min(list_manas)

def part_2(input) : 
    list_manas = []
    player_turn([], 50 , 500 ,  input[0], input[1] , 0 , True, list_manas)
    return min(list_manas)


    
def player_turn(effects_t, player_hp, player_mana,  boss_hp, boss_damage, spent_mana, hard_mode, list_manas):
    effects = copy.deepcopy(effects_t)
    
    # Damages application
    player_damage = sum([effect[2] for effect in effects])
    boss_hp -= player_damage
    player_hp -= hard_mode
    if player_hp <= 0 : return 
    if boss_hp <= 0 : 
        list_manas.append(spent_mana)
        return
    
    # Recharge mana
    player_mana +=  sum([effect[4] for effect in effects])
    
    # Effects Update
    for effect in effects :
        effect[1] -= 1

    for effect in effects :
        if effect[1] == 0 : 
            effects.remove(effect)
        
     # New cast   
    if player_mana < 53 : return
    le = [effect[0] for effect in effects]
    if player_mana >= 53 : boss_turn(effects, player_hp, player_mana - 53,  boss_hp - 4, boss_damage, spent_mana + 53, hard_mode, list_manas)
    if player_mana >= 73 : boss_turn(effects, player_hp + 2, player_mana - 73,  boss_hp - 2, boss_damage, spent_mana + 73, hard_mode, list_manas)
    if player_mana >= 229 and 229 not in le: boss_turn(effects + [[229 , 5, 0, 0, 101]], player_hp, player_mana - 229,  boss_hp , boss_damage, spent_mana + 229, hard_mode, list_manas) 
    if player_mana >= 113 and 113 not in le: boss_turn(effects + [[113 , 6, 0, 7, 0]], player_hp, player_mana - 113,  boss_hp , boss_damage, spent_mana + 113, hard_mode, list_manas) 
    if player_mana >= 173 and 173 not in le: boss_turn(effects + [[173, 6, 3, 0, 0]], player_hp, player_mana - 173,  boss_hp , boss_damage, spent_mana + 173, hard_mode, list_manas) 





def boss_turn(effects_t, player_hp, player_mana,  boss_hp, boss_damage, spent_mana, hard_mode, list_manas):
    effects = copy.deepcopy(effects_t)

    if list_manas!= [] and spent_mana > min(list_manas): return 
    
    # Damage application application
    player_damage = sum([effect[2] for effect in effects])
    boss_hp -= player_damage
    if boss_hp <= 0 :
        list_manas.append(spent_mana)
        return 
    
    # Recharge mana
    player_mana +=  sum([effect[4] for effect in effects])

    # Boss attack
    player_hp -= max(1, boss_damage - sum([effect[3] for effect in effects]))
    if player_hp <= 0 : 
        return 
    
    # Effects update
    for effect in effects :
        effect[1] -= 1

    for effect in effects :
        if effect[1] == 0 : 
            effects.remove(effect)
        
    return player_turn(effects, player_hp, player_mana,  boss_hp, boss_damage, spent_mana, hard_mode, list_manas)