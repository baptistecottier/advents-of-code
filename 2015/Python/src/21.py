with open("Day21/input") as f:
    weapons , armor ,rings =[[[item for item in weapon.split(' ') if item != ''] for weapon in things] for things in [item.split('\n')[1:] for item in f.read().split('\n\n')]]
    print(weapons, armor, rings)



best_cost=500
worst_cost=0
for weapon in weapons : 
    for arm in armor+[['None' , '0' , '0', '0']] : 
        for ring_a in rings + [['None' , '+0', '0' , '0', '0']]:
            for ring_b in [item for item in rings if item != ring_a]+ [['None' , '+0', '0' , '0', '0']]:
                player_hp = 100 
                boss_hp = 109
                boss_damage = 8
                boss_armor = 2
                cost=int(weapon[1])+int(arm[1])+int(ring_a[2])+int(ring_b[2])
                damage=int(weapon[2])+int(ring_a[3])+int(ring_b[3])
                armo=int(arm[3])+int(ring_a[4])+int(ring_b[4])
                while(player_hp > 0 and boss_hp > 0):
                    boss_hp=boss_hp-max(1,damage-boss_armor)
                    if boss_hp > 0 : player_hp=player_hp - max(1,boss_damage-armo)
                if boss_hp <=0  : best_cost=min(best_cost, cost)
                elif player_hp <= 0 : worst_cost=max(worst_cost, cost)
print("PART I :",best_cost)
print("PART II :",worst_cost)