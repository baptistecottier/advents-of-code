from itertools import product, combinations

class Item:
    def __init__(self, cost, damage, armor) -> None:
        self.cost = cost
        self.damage = damage
        self.armor = armor
    
class Player:
    def __init__(self, hp, damage, armor) -> None:
        self.hp = hp
        self.damage = damage
        self.armor = armor
    
def generator(input):
    (hp, damage, armor) = (int(item.split(": ")[1]) for item in input.splitlines())
    return hp, damage, armor

def part_1(boss_stats): 
    return min(test_all_fights(*boss_stats)["win"])

def part_2(boss_stats):    
    return max(test_all_fights(*boss_stats)["lose"])


def test_all_fights(boss_hp, boss_damage, boss_armor):
    WEAPONS =   {Item(8, 4, 0), Item(10, 5, 0), Item(25, 6, 0), Item(40, 7, 0), Item(74, 8, 0)}
    ARMORS =    {Item(0, 0, 0), Item(13, 0, 1), Item(31, 0, 2), Item(53, 0, 3), Item(75, 0, 4), Item(102, 0, 5)}
    RINGS =     {Item(0, 0, 0), Item(0, 0, 0),  Item(20, 0, 1), Item(25, 1, 0), Item(40, 0, 2), Item(50, 2, 0), Item(80, 0, 3), Item(100, 3, 0)}
    
    costs = {"win": set(), "lose": set()}

    for (weapon, armor, (left_ring, right_ring)) in product(WEAPONS, ARMORS, combinations(RINGS, 2)):
        
            player          = Player(100, 0, 0)
            player.damage   = max(1, sum(item.damage for item in (weapon, armor, left_ring, right_ring)) - boss_armor)
            player.armor    = sum(item.armor  for item in (weapon, armor, left_ring, right_ring))

            boss            = Player(boss_hp, max(1, boss_damage - player.armor), boss_armor)
            
            while boss.hp > 0 and player.hp > 0:
                boss.hp     -= player.damage
                player.hp   -= boss.damage
            
            if boss.hp <= 0: 
                costs["win"].add(sum(item.cost for item in (weapon, armor, left_ring, right_ring)))
            else:            
                costs["lose"].add(sum(item.cost for item in (weapon, armor, left_ring, right_ring)))
    return costs