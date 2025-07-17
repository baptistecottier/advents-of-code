"""Advent of Code - Year 2015 - Day 22"""

from collections.abc import Iterator
from copy import deepcopy
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
    """
    Boss class representing the adversary in a game.

    Attributes:
        hp (int): Health points of the boss.
        damage (int): Damage points that boss can inflict on opponents.
    """

    hp: int
    damage: int


def preprocessing(puzzle_input: str) -> Boss:
    """
    Parses the puzzle input string and returns a Boss instance with hit points and damage.

    Args:
        puzzle_input (str): Multiline string with boss stats in the format:
                            "Hit Points: X
                            Damage: Y".

    Returns:
        Boss: An instance of Boss initialized with parsed hit points and damage.

    Example:
        >>> preprocessing("Hit Points: 55\nDamage: 8")
        Boss(hp=55, damage=8)
    """
    (hp, damage) = (int(item.split(": ")[1]) for item in puzzle_input.splitlines())
    return Boss(hp, damage)


def solver(boss: Boss) -> Iterator[int]:
    """
    Solves the boss fight puzzle for both normal and hard modes, yielding the minimum mana spent to
    win.

    Args:
        boss (Boss): The boss character to fight.

    Yields:
        int: The minimum mana required to win in each mode (normal, hard).

    Example:
        >>> boss = Boss(hp=55, damage=8)
        >>> list(solver(boss))
        [953, 1289]
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
    winning_manas: set[int],
) -> None:
    """
    Simulates the player's turn in the turn-based battle, applying spell effects, handling spell
    casting, and updating game state.

    Args:
        spells (list[list[int]]): List of active spells, each represented as a list of spell
                                  attributes.
        player (Player): The current state of the player (hp, mana, spent).
        boss (Boss): The current state of the boss (hp, damage).
        hard_mode (bool): If True, player loses 1 hp at the start of their turn.
        winning_manas (set[int]): Set to collect mana costs of winning strategies.

    Returns:
        None
    """
    player.hp = player.hp - hard_mode
    if player.hp <= 0:
        return None

    boss.hp = boss.hp - sum(spell[2] for spell in spells)
    if boss.hp <= 0:
        winning_manas.add(player.spent)
        return None

    player.mana += sum(spell[4] for spell in spells)

    spells = [spell for spell in spells if spell[1] > 1]
    for spell in spells:
        spell[1] -= 1

    if player.mana < 53:
        return None

    for cost, php, bdmg in [[53, 0, 4], [73, 2, 2]]:
        if player.mana >= cost:
            boss_turn(
                deepcopy(spells),
                Player(player.hp + php, player.mana - cost, player.spent + cost),
                Boss(boss.hp - bdmg, boss.damage),
                hard_mode,
                winning_manas,
            )

    ongoing_spells = [spell[0] for spell in spells]
    for spell in [[113, 6, 0, 7, 0], [173, 6, 3, 0, 0], [229, 5, 0, 0, 101]]:
        if spell[0] not in ongoing_spells:
            boss_turn(
                deepcopy(spells) + [spell],
                Player(player.hp, player.mana - spell[0], player.spent + spell[0]),
                Boss(boss.hp, boss.damage),
                hard_mode,
                winning_manas,
            )

    return None


def boss_turn(
    spells: list[list[int]],
    player: Player,
    boss: Boss,
    hard_mode: bool,
    winning_manas: set[int],
) -> None:
    """
    Executes the boss's turn in the game, applying active spell effects, updating player and boss
    stats, and determining if the game should continue or end.

    Args:
        spells (list[list[int]]): List of active spells, each represented as a list of spell
                                  attributes.
        player (Player): The player object, with current stats.
        boss (Boss): The boss object, with current stats.
        hard_mode (bool): Whether the game is in hard mode.
        winning_manas (set[int]): Set of mana values representing winning outcomes.

    Returns:
        None or result of player_turn: Returns None if the game ends, otherwise proceeds to the
                                       player's turn.

    Example:
        >>> boss_turn(active_spells, player, boss, False, set())
    """
    if winning_manas != set() and player.spent > min(winning_manas):
        return None

    boss.hp = boss.hp - sum(spell[2] for spell in spells)
    if boss.hp <= 0:
        winning_manas.add(player.spent)
        return None

    player.hp = player.hp - max(1, boss.damage - sum(spell[3] for spell in spells))
    if player.hp <= 0:
        return None

    player.mana += sum(spell[4] for spell in spells)

    spells = [spell for spell in spells if spell[1] > 1]
    for spell in spells:
        spell[1] -= 1

    return player_turn(deepcopy(spells), player, boss, hard_mode, winning_manas)
