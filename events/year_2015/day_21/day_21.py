"""Advent of Code - Year 2015 - Day 21"""

from itertools import product, combinations
from dataclasses import dataclass

@dataclass(unsafe_hash = True)
class Item:
    """
    Represents an item with cost, damage, and armor attributes.
    """
    cost: int
    damage: int
    armor: int


@dataclass
class Player:
    """
    Player class representing an entity in the game with health points, damage, and armor
    attributes.
    """
    hp: int
    damage: int
    armor: int


def preprocessing(puzzle_input: str) -> tuple[int, int, int]:
    """
    Extract key stats from the puzzle input.

    Args:
        puzzle_input (str): The puzzle input containing HP, damage, and armor values.

    Returns:
        tuple[int, int, int]: The extracted hit points, damage, and armor values.
    """
    (hp, damage, armor) = (int(item.split(": ")[1]) for item in puzzle_input.splitlines())
    return hp, damage, armor


def solver(hp: int, damage: int, armor: int):
    """
    Computes the minimum cost to win and maximum cost to lose against a boss.
    
    Args:
        *boss_stats: A tuple containing boss statistics (hit points, damage, armor)
    
    Yields:
        int: First, the minimum cost to win a fight
        int: Second, the maximum cost to lose a fight
    """
    costs = simulate_all_fights(hp, damage, armor)
    yield min(costs[True])
    yield max(costs[False])


def simulate_all_fights(boss_hp: int, boss_damage: int, boss_armor: int) -> dict[bool, set]:
    """
    Simulates all possible equipment combinations against a boss and returns the costs for wins and
    losses.
    
    Args:
        boss_hp: The boss's hit points
        boss_damage: The boss's damage
        boss_armor: The boss's armor
        
    Returns:
        A dictionary with keys 0 and 1 containing sets of costs where:
        - costs[False]: costs of equipment combinations that result in player losing
        - costs[True]: costs of equipment combinations that result in player winning
    """
    weapons =   {Item(8, 4, 0) , Item(10, 5, 0), Item(25, 6, 0), Item(40, 7, 0),
                 Item(74, 8, 0)}

    armors =    {Item(0, 0, 0) , Item(13, 0, 1), Item(31, 0, 2), Item(53, 0, 3),
                 Item(75, 0, 4), Item(102, 0, 5)}

    rings =     {Item(0, 0, 0) , Item(0, 0, 0) , Item(20, 0, 1), Item(25, 1, 0),
                 Item(40, 0, 2), Item(50, 2, 0), Item(80, 0, 3), Item(100, 3, 0)}

    costs = {False: set(), True: set()}

    for (weapon, armor, (left_ring, right_ring)) in product(weapons,
                                                            armors,
                                                            combinations(rings, 2)):
        equipment = (weapon, armor, left_ring, right_ring)
        player = Player(100,
                        max(1, sum(item.damage for item in equipment) - boss_armor),
                        sum(item.armor  for item in equipment))
        boss = Player(boss_hp, max(1, boss_damage - player.armor), boss_armor)

        while boss.hp > 0 and player.hp > 0:
            boss.hp -= player.damage
            player.hp -= boss.damage
        costs[boss.hp <= 0].add(sum(item.cost for item in equipment))

    return costs
