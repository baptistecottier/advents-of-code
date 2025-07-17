"""Advent of Code - Year 2015 - Day 21"""

from dataclasses import dataclass
from itertools import product, combinations


@dataclass(unsafe_hash=True)
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
    Parses the puzzle input and extracts hit points, damage, and armor values.

    Args:
        puzzle_input (str): Multiline string with each line in the format 'Label: value'.

    Returns:
        tuple[int, int, int]: A tuple containing (hp, damage, armor) as integers.

    Example:
        >>> preprocessing("Hit Points: 100\nDamage: 8\nArmor: 2")
        (100, 8, 2)
    """
    (hp, damage, armor) = (
        int(item.split(": ")[1]) for item in puzzle_input.splitlines()
    )
    return hp, damage, armor


def solver(hp: int, damage: int, armor: int) -> tuple[int, int]:
    """
    Simulates all possible fights and returns the minimum cost to win and the maximum cost to lose.

    Args:
        hp (int): The player's hit points.
        damage (int): The player's damage value.
        armor (int): The player's armor value.

    Returns:
        tuple[int, int]: A tuple containing the minimum cost to win and the maximum cost to lose.

    Examples:
        >>> solver(100, 8, 5)
        (78, 148)
    """
    costs_if_player_wins = simulate_all_fights(hp, damage, armor)
    return min(costs_if_player_wins[True]), max(costs_if_player_wins[False])


def simulate_all_fights(
    boss_hp: int, boss_damage: int, boss_armor: int
) -> dict[bool, set]:
    """
    Simulates all possible fights between the player and the boss using different equipment
    combinations.

    Args:
        boss_hp (int): The hit points of the boss.
        boss_damage (int): The damage value of the boss.
        boss_armor (int): The armor value of the boss.

    Returns:
        dict[bool, set]: A dictionary mapping True (player wins) and False (player loses) to sets
                         of total equipment costs.

    Example:
        >>> results = simulate_all_fights(100, 8, 2)
        >>> results
        {True: {78, 95, 102, ...}, False: {148, 153, ...}}
    """
    weapons = {
        Item(8, 4, 0),
        Item(10, 5, 0),
        Item(25, 6, 0),
        Item(40, 7, 0),
        Item(74, 8, 0),
    }

    armors = {
        Item(0, 0, 0),
        Item(13, 0, 1),
        Item(31, 0, 2),
        Item(53, 0, 3),
        Item(75, 0, 4),
        Item(102, 0, 5),
    }

    rings = {
        Item(0, 0, 0),
        Item(0, 0, 0),
        Item(20, 0, 1),
        Item(25, 1, 0),
        Item(40, 0, 2),
        Item(50, 2, 0),
        Item(80, 0, 3),
        Item(100, 3, 0),
    }

    costs = {False: set(), True: set()}

    for weapon, armor, (left_ring, right_ring) in product(
        weapons, armors, combinations(rings, 2)
    ):
        equipment = (weapon, armor, left_ring, right_ring)
        player = Player(
            100,
            max(1, sum(item.damage for item in equipment) - boss_armor),
            sum(item.armor for item in equipment),
        )
        boss = Player(boss_hp, max(1, boss_damage - player.armor), boss_armor)

        while boss.hp > 0 and player.hp > 0:
            boss.hp -= player.damage
            player.hp -= boss.damage
        costs[boss.hp <= 0].add(sum(item.cost for item in equipment))

    return costs
