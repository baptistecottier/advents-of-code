"""Advent of Code - Year 2015 - Day 22"""

import copy
from dataclasses import dataclass

@dataclass
class Player:
    """
    Player class representing participants in a game.

    Attributes:
        hp (int): Health points of the player.
        mana (int): Mana points available for casting spells.
        spent (int): Total mana spent by the player.
    """
    hp: int
    mana: int
    spent: int


@dataclass
class Boss:
    """Boss class representing the adversary in a game.

    Attributes:
        hp (int): Health points of the boss.
        damage (int): Damage points that boss can inflict on opponents.
    """
    hp: int
    damage: int

def preprocessing(puzzle_input: str) -> Boss:
    """
    Parse the puzzle input to extract the hit points and damage of the boss.
    """
    (hp, damage) = (int(item.split(": ")[1]) for item in puzzle_input.splitlines())
    return Boss(hp, damage)


def solver(boss: Boss):
    """
    Solve the two parts of the Wizard Simulator 20XX puzzle by finding the minimum mana required to
    defeat the boss.
    """
    player = Player(50, 500, 0)

    for hard_mode in [False, True]:
        player_turn([], player, boss, hard_mode, winning_manas := set())
        yield min(winning_manas)


def player_turn(
    spells: list[list[int]],
    player: Player,
    boss: Boss,
    hard_mode: bool,
    winning_manas: set[int]):
    """
    Handle the player's turn in a magic duel against the boss, applying spells and casting
    spells.
    """
    player.hp = player.hp - hard_mode
    if player.hp <= 0:
        return
    boss.hp = boss.hp - sum(spell[2] for spell in spells)
    if boss.hp <= 0:
        winning_manas.add(player.spent)
        return

    player.mana += sum(spell[4] for spell in spells)

    spells = [spell for spell in spells if spell[1] > 1]
    for spell in spells :
        spell[1] -= 1

    if player.mana < 53:
        return

    for cost, php, bdmg in [[53, 0, 4], [73, 2, 2]]:
        if player.mana >= cost:
            boss_turn(
                copy.deepcopy(spells),
                Player(player.hp + php, player.mana - cost, player.spent + cost),
                Boss(boss.hp - bdmg, boss.damage),
                hard_mode,
                winning_manas)

    ongoing_spells = [spell[0] for spell in spells]
    for spell in [[113 , 6, 0, 7, 0], [173, 6, 3, 0, 0], [229 , 5, 0, 0, 101]]:
        if spell[0] not in ongoing_spells:
            boss_turn(
                copy.deepcopy(spells) + [spell],
                Player(player.hp, player.mana - spell[0], player.spent + spell[0]),
                Boss(boss.hp, boss.damage),
                hard_mode,
                winning_manas)


def boss_turn(
    spells: list[list[int]],
    player: Player,
    boss: Boss,
    hard_mode: bool,
    winning_manas: set[int]):
    """
    Handle the boss turn phase, updating spells, health, mana, and determining game outcome.
    """
    if winning_manas!= set() and player.spent > min(winning_manas):
        return None
    boss.hp = boss.hp - sum(spell[2] for spell in spells)
    if boss.hp <= 0:
        winning_manas.add(player.spent)
        return None
    player.hp = player.hp -  max(1, boss.damage - sum(spell[3] for spell in spells))
    if player.hp <= 0:
        return None

    player.mana += sum(spell[4] for spell in spells)

    spells = [spell for spell in spells if spell[1] > 1]
    for spell in spells :
        spell[1] -= 1

    return player_turn(
        copy.deepcopy(spells),
        player,
        boss,
        hard_mode,
        winning_manas)
