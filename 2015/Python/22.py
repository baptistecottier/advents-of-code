# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.


# Name, cost, armor, damage, rounds, hit points, mana


spells={
    'Missile': {'mana' : 53, 'armor': 0, 'damage' : 4, 'turns' : 1, 'hp' : 0, 'new_mana' : 0 },
    'Drain': {'mana' : 73, 'armor': 0, 'damage' : 2, 'turns' : 1, 'hp' : 2, 'new_mana' : 0 }, 
    'Shield': {'mana' : 113, 'armor': 7, 'damage' : 0, 'turns' : 6, 'hp' : 0, 'new_mana' : 0 }, 
    'Poison': {'mana' : 173, 'armor': 0, 'damage' : 3, 'turns' : 6, 'hp' : 0, 'new_mana' : 0 }, 
    'Recharge': {'mana' : 229, 'armor': 0, 'damage' : 0, 'turns' : 5, 'hp' : 0, 'new_mana' : 101 }
}
def print_player(player_hp, player_armor, mana, boss_hp, current_spells):
    print("-- Player turn --")
    print(" Player has",player_hp, "hit points,", player_armor, "armor,", mana, "mana")
    print("Boss has", boss_hp, "hit points")
    for spell in current_spells:
        print("Spell :",spell)

def print_boss(player_hp, player_armor, mana, boss_hp, current_spells):
    print("-- Boss turn --")
    print(" Player has",player_hp, "hit points,", player_armor, "armor,", mana, "mana")
    print("Boss has", boss_hp, "hit points")

for spell in [spells[3]]: 
    print_player(player_hp=10, player_armor=0, mana=250, boss_hp=13, current_spells=spell)
    fight(list([spell]).copy(), spells.copy(), [13, 8] , 10, 250-spell[1] , spell[1])


# 245 too low