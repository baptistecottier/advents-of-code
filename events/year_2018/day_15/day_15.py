"""
Advent of Code - Year 2018 - Day 15
https://adventofcode.com/2018/day/15
"""

# Standard imports
from collections import deque
from dataclasses import dataclass, replace

# First-party imports
from pythonfw import functions as aocf


@dataclass
class Unit:
    """
    A class to represent a Unit in the game.
    Attributes:
        id (int): The unique identifier for the unit.
        x (int): The x-coordinate of the unit's position.
        y (int): The y-coordinate of the unit's position.
        type (str): The type of the unit (e.g., 'Elf', 'Goblin').
        hp (int): The hit points (health) of the unit.
    """
    id: int
    x: int
    y: int
    type: str
    hp: int

    def xy(self):
        """Returns the coordinates as a tuple (x, y)."""
        return (self.x, self.y)


def preprocessing(puzzle_input: str) -> tuple[list[Unit], set[tuple[int, int]]]:
    """
    Preprocesses the puzzle input to extract units and cave walls.

    Args:
        puzzle_input (str): The input string representing the cave layout.

    Returns:
        tuple: A tuple containing:
            - units (list[Unit]): A list of Unit objects representing the units in the cave.
            - cave (set): A set of tuples representing the coordinates of the cave walls.
    """
    n_id = 0
    cave: set = set()
    units: list[Unit] = []
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(line):
            if char == '#':
                cave.add((x, y))
            elif char in 'EG':
                units.append(Unit(n_id, x, y, char, 200))
                n_id += 1
    return units, cave


def solver(units: list[Unit], cave: set[tuple[int, int]]):
    """
    Solves the combat simulation problem for both parts of the puzzle.
    This function simulates combat between elves and goblins in a cave system. It solves both:
    1. The original combat scenario
    2. The minimum attack power needed for elves to win without any casualties
    Args:
        units (list): List of unit objects representing elves and goblins with their positions and
                      attributes
        cave (list): 2D grid representation of the cave system where combat takes place
    Yields:
        int: Two values are yielded:
            1. The outcome of the original combat (rounds completed * sum of remaining HP)
            2. The outcome when elves have minimum attack power needed to win without losses
    Notes:
        - Uses binary search to find the minimum elf attack power needed
        - The second part ensures no elf casualties by retrying with different attack powers
        - Attack power search range is between 3 and 200
    """
    yield fight([replace(u) for u in units], cave)

    size = 3
    r = 200
    outcomes = {}

    while r - size > 1:
        elf_pa = (size + r) // 2
        copied_units = [replace(u) for u in units]
        outcome = fight(copied_units, cave, True, elf_pa)
        if outcome == -1:
            size = elf_pa
        else:
            outcomes[elf_pa] = outcome
            r = elf_pa

    yield outcomes[min(outcomes.keys())]


def fight(
        units: list[Unit],
        cave: set[tuple[int, int]],
        no_elf_loss: bool = False,
        elf_power_attack: int = 3) -> int:
    """
    Simulates a fight between units in a cave, returning the outcome score or -1 if elves lose when
    no_elf_loss is True.
    """
    n_round = 0
    while not is_fight_over(units):
        units = sorted_units(units)
        for unit in units:
            if unit.hp <= 0:
                continue

            min_dist, target = move(unit, units, cave)

            if min_dist <= 1 and target is not None:
                for u in units:
                    if (aocf.manhattan(u.xy(), unit.xy()) == 1
                            and u.type != unit.type
                            and 0 < u.hp < target.hp):
                        target = u

                if target.type == 'E':
                    target.hp -= 3
                    if target.hp <= 0 and no_elf_loss:
                        return -1
                else:
                    target.hp -= elf_power_attack

                if is_fight_over(units):
                    return (n_round + (unit == units[-1])) * sum(u.hp for u in units if u.hp > 0)
        n_round += 1
    return -1


def is_fight_over(units: list[Unit]) -> bool:
    """Returns True if only one unit type remains alive, indicating the fight is over."""
    return len(set({u.type for u in units if u.hp > 0})) == 1


def sorted_units(units: list[Unit]) -> list[Unit]:
    """
    Returns a list of living units sorted by reading order (top-to-bottom, left-to-right).
    """
    units = [u for u in units if u.hp > 0]
    return sorted(units, key=lambda u: (u.y, u.x))


def find_closest_adversary(start, cave: set, units, adv_type) -> tuple[int, Unit | None]:
    """
    Find the closest adversary of the specified type using BFS pathfinding.
    """
    adversaries_position = {}

    for u in units:
        if u.hp > 0:
            if u.type == adv_type:
                adversaries_position[(u.x, u.y)] = u
            else:
                cave.add((u.x, u.y))

    if start in cave:
        return (-1, None)

    queue = deque([[start]])
    seen = set([start])

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) in adversaries_position:
            return (len(path) - 1, adversaries_position[(x, y)])
        for x2, y2 in ((x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)):
            if (x2, y2) not in seen and (x2, y2) not in cave and (x2 > 0 and y2 > 0):
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

    return (-1, None)


def move(unit: Unit, units: list[Unit], cave: set[tuple[int, int]]) -> tuple[int, Unit | None]:
    """
    Moves a unit towards the closest adversary and returns the distance and target.
    """
    target = None
    adv_type = {'G': 'E', 'E': 'G'}
    ux = nx = unit.x
    uy = ny = unit.y
    min_dist = 1_000

    for start in [(ux, uy - 1), (ux - 1, uy), (ux + 1, uy), (ux, uy + 1)]:
        adv_dist, adv_unit = find_closest_adversary(
                                start,
                                cave.copy(),
                                units,
                                adv_type[unit.type])
        if 0 <= adv_dist < min_dist:
            target = adv_unit
            nx, ny = start
            min_dist = adv_dist

    if min_dist > 0:
        unit.x = nx
        unit.y = ny

    return min_dist, target
