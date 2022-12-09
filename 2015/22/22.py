import sys
import numpy as np
import copy

def generator(specs) : 
    s=[]
    for spec in specs.splitlines() : 
        s.append(int(spec.split(': ')[1]))
    return s

def part_1(input) : 
    manas = player_turn([], 10, 250 , 13, 8 , 0 , False)
    return min(eval('['+str(manas).replace('[','').replace(']','')+']'))

def part_2(input) : 
    2
    
def player_turn(effects, player_hp, player_mana,  boss_hp, boss_damage, spent_mana, hard_mode):
    print("Player :", player_hp, boss_hp)
    # Damages application
    player_damage = sum([effect[2][0] for effect in effects])
    boss_hp -= player_damage
    if boss_hp <= 0 : return spent_mana
    if hard_mode : 
        player_hp -= hard_mode
    
    # Recharge mana
    player_mana +=  sum([effect[4] for effect in effects])
    
    # Effects Update
    for effect in effects :
        if effect[1] == 1 : effects.remove(effect)
        else : effect[1] -= 1
        
     # New cast   
    le = [effect[0] for effect in effects]
    a, b, c, d, e = 5000, 5000, 5000, 5000, 5000
    if player_mana < 53 : return sys.maxsize
    a = boss_turn([item for item in effects], player_hp, player_mana - 53,  boss_hp, boss_damage, spent_mana + 53, hard_mode)
    if player_mana >= 73 : b = boss_turn([item for item in effects], player_hp + 2, player_mana - 73,  boss_hp - 2, boss_damage, spent_mana + 73, hard_mode)
    if player_mana >= 229 :e = boss_turn([item for item in effects] + [[229 , 5, [0, 0], 0, 101]], player_hp, player_mana - 229,  boss_hp , boss_damage, spent_mana + 229, hard_mode) 
    if player_mana >= 113 :c = boss_turn([item for item in effects] + [[113 , 6, [0, 0], 7, 0]], player_hp, player_mana - 113,  boss_hp , boss_damage, spent_mana + 113, hard_mode) 
    if player_mana >= 173 :d = boss_turn([item for item in effects] + [[173, 6, [3, 0], 0, 0]], player_hp, player_mana - 173,  boss_hp , boss_damage, spent_mana + 173, hard_mode) 
    return min([a,b,c,d,e])





def boss_turn(effects, player_hp, player_mana,  boss_hp, boss_damage, spent_mana, hard_mode):
    print("Boss :", player_hp, boss_hp)
    if player_mana < 0 : return sys.maxsize
    if spent_mana > 2000 : return 2000
    # Damage application application
    player_damage = sum([effect[2][0] for effect in effects])
    boss_hp -= player_damage
    if boss_hp <= 0 : return spent_mana
    
    # Recharge mana
    player_mana +=  sum([effect[4] for effect in effects])
    
    # Boss attack
    player_hp -= max(1, boss_damage - sum([effect[3] for effect in effects]))
    if player_hp <= 0 : return sys.maxsize
    
    # Effect update
    for effect in effects :
        if effect[1] == 1 : effects.remove(effect)
        else : effect[1] -= 1
        
    return player_turn([item for item in effects], player_hp, player_mana,  boss_hp, boss_damage, spent_mana, hard_mode)

def bfs(maze, start , end):
    width , height = len(maze[0]) , len(maze)
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x , y) == end:
            return len(path)-1
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and maze[y2][x2] != '#' and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))