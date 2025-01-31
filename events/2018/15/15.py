from collections import deque
from dataclasses import dataclass, replace
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


def preprocessing(puzzle_input):
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
    units: list[Unit] = list()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(line):
            if char == '#':
                cave.add((x, y))
            elif char in 'EG':
                units.append(Unit(n_id, x, y, char, 200))
                n_id += 1
    return units, cave


def solver(units, cave):
    """Solves the combat simulation problem for both parts of the puzzle.
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

    l = 3
    r = 200
    outcomes = {}
    while r - l > 1:
        elf_pa = (l + r) // 2
        copied_units = [replace(u) for u in units]
        outcome = fight(copied_units, cave, True, elf_pa)
        if outcome == -1:
            l = elf_pa
        else:
            outcomes[elf_pa] = outcome
            r = elf_pa
    yield outcomes[min(outcomes.keys())]


def fight(units, cave, no_elf_loss = False, elf_power_attack = 3):
    '''
    Simulates a combat between elves and goblins on a cave map.

    The function processes rounds of combat where units move and attack according to specific rules.
    Units can move to engage the nearest enemy and attack when adjacent.

    Parameters:
        units (list): List of Unit objects representing all combatants
        cave (list): 2D list representing the cave layout
        no_elf_loss (bool): If True, function returns -1 if any elf dies. Defaults to False
        elf_power_attack (int): Attack power for elves. Defaults to 3

    Returns:
        int: Either:
            - The combat outcome (number of complete rounds * sum of remaining HP) if combat 
              completes
            - -1 if no_elf_loss is True and an elf dies

    Notes:
        - Units take turns in reading order (top-to-bottom, left-to-right)
        - Each unit can move and attack once per round
        - Combat ends when one side is eliminated
        - Elves deal elf_power_attack damage, Goblins always deal 3 damage
    '''
    n_round = 0
    while not is_fight_over(units):
        units = sorted_units(units)
        for unit in units:
            if unit.hp <= 0:
                continue

            min_dist, target = move(unit, units, cave)

            if min_dist <= 1:
                for u in units:
                    if (aocf.manhattan(u, unit) == 1
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

def is_fight_over(units):
    """
    Count the number of unique unit types that have a positive hit point (hp) value.
    Args:
        units (list): A list of unit objects, where each unit has attributes 'type' and 'hp'.
    Returns:
        int: The number of unique unit types with hp greater than 0.
    """
    return len(set({u.type for u in units if u.hp > 0})) == 1


def sorted_units(units):
    """
    Sort and filter units based on their position and health.
    Args:
        units (list): List of unit objects with attributes hp, x, and y.
    Returns:
        list: Filtered and sorted list of units. Units are first filtered to include only
              those with hp > 0, then sorted by y coordinate first and x coordinate second.
    """
    units = [u for u in units if u.hp > 0]
    return sorted(units, key = lambda u: (u.y, u.x))


def find_closest_adversary(start, cave: set, units, adv_type):
    """
    Find the closest adversary unit from a starting position in a cave system.
    Parameters:
        start (tuple): A tuple (x, y) representing the starting position
        cave (set): A set of tuples (x, y) representing wall positions in the cave
        units (list): A list of Unit objects representing all units in the game
        adv_type (str): The type of adversary to search for ('E' for Elf or 'G' for Goblin)
    Returns:
        tuple: A tuple containing:
            - int: The distance to the closest adversary (-1 if no adversary found)
            - Unit or None: The closest adversary Unit object (None if no adversary found)
    Notes:
        - Uses breadth-first search to find the shortest path to an adversary
        - Considers only valid moves (up, left, right, down) within cave boundaries
        - Avoids walls and other units' positions
        - Returns (-1, None) if start position is in cave or no path to adversary exists
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


def move(unit, units, cave):
    """Move a unit towards the closest enemy.
    This function determines the next position for a unit by evaluating possible moves
    towards the nearest enemy unit. The unit can move one step in any of the four
    cardinal directions (up, left, right, down).
    Args:
        unit: The unit object to be moved
        units: List of all units in the game
        cave: 2D map representation of the game area
    Returns:
        tuple: A pair containing:
            - minimum distance to closest enemy (int)
            - target enemy unit object (Unit or None if no enemy is reachable)
    Movement Rules:
    - Units can only move to adjacent empty squares
    - Units will move towards the nearest enemy
    - If multiple enemies are equidistant, movement priority is reading order
      (top-to-bottom, left-to-right)
    - If no enemies are reachable, unit stays in place
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
