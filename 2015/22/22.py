import copy


def preprocessing(input_):
    (hp, damage) = (int(item.split(": ")[1]) for item in input_.splitlines())
    return hp, damage


def solver(boss_data): 
    player_turn([], 50, 500, *boss_data, 0, False, list_manas := set())
    yield min(list_manas)

    player_turn([], 50, 500, *boss_data, 0, True, list_manas := set())
    yield min(list_manas)


def player_turn(effects, player_hp, player_mana,  boss_hp, boss_damage, spent_mana, hard_mode, list_manas):
    
    if (player_hp:= player_hp - hard_mode) <= 0: 
        return 
    
    if (boss_hp:= boss_hp - sum(effect[2] for effect in effects)) <= 0: 
        list_manas.add(spent_mana)
        return
    
    player_mana += sum(effect[4] for effect in effects)
    
    effects = [effect for effect in effects if effect[1] > 1]
    for effect in effects :
        effect[1] -= 1   
             
    if player_mana < 53 : return
    if player_mana >= 53 : boss_turn(copy.deepcopy(effects), player_hp, player_mana - 53,  boss_hp - 4, boss_damage, spent_mana + 53, hard_mode, list_manas)
    if player_mana >= 73 : boss_turn(copy.deepcopy(effects), player_hp + 2, player_mana - 73,  boss_hp - 2, boss_damage, spent_mana + 73, hard_mode, list_manas)
    
    le = [effect[0] for effect in effects]
    if player_mana >= 113 and 113 not in le: 
        boss_turn(copy.deepcopy(effects) + [[113 , 6, 0, 7, 0]], player_hp, player_mana - 113,  boss_hp , boss_damage, spent_mana + 113, hard_mode, list_manas) 
    if player_mana >= 173 and 173 not in le: 
        boss_turn(copy.deepcopy(effects) + [[173, 6, 3, 0, 0]], player_hp, player_mana - 173,  boss_hp , boss_damage, spent_mana + 173, hard_mode, list_manas) 
    if player_mana >= 229 and 229 not in le: 
        boss_turn(copy.deepcopy(effects) + [[229 , 5, 0, 0, 101]], player_hp, player_mana - 229,  boss_hp , boss_damage, spent_mana + 229, hard_mode, list_manas) 


def boss_turn(effects, player_hp, player_mana,  boss_hp, boss_damage, spent_mana, hard_mode, list_manas):

    if list_manas!= set() and spent_mana > min(list_manas): 
        return 
    
    if (boss_hp:= boss_hp - sum(effect[2] for effect in effects)) <= 0 :
        list_manas.add(spent_mana)
        return 
    
    if (player_hp := player_hp -  max(1, boss_damage - sum(effect[3] for effect in effects))) <= 0 : 
        return 
    
    player_mana += sum(effect[4] for effect in effects)
    
    effects = [effect for effect in effects if effect[1] > 1]
    for effect in effects :
        effect[1] -= 1   
        
    return player_turn(copy.deepcopy(effects), player_hp, player_mana,  boss_hp, boss_damage, spent_mana, hard_mode, list_manas)