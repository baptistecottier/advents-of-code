from dataclasses import dataclass, replace
from parse       import parse

@dataclass(unsafe_hash = True)
class Unit:
    size: int
    hp: int
    damage: int
    attack_type: str
    initiative: int
    weakness: list[str]
    immunities: list[str]

    @property
    def effective_power(self):
        """
        Calculate the effective power of the group.

        The effective power is determined by multiplying the size of the group
        by the damage it can deal.

        Returns:
            int: The effective power of the group.
        """
        return self.size * self.damage


def preprocessing(puzzle_input):
    """
    Preprocesses the puzzle input to extract immune and infection units.
    Args:
        puzzle_input (str): The raw input string containing two sections separated by a double
                            newline.
                            The first section represents the immune system units and the second 
                            section represents the infection units.
    Returns:
        tuple: A tuple containing two lists:
               - immune_units (list): A list of immune system units extracted from the input.
               - infect_units (list): A list of infection units extracted from the input.
    """

    immune, infect = puzzle_input.split("\n\n")
    immune_units = extract_groups(immune)
    infect_units = extract_groups(infect)
    return immune_units, infect_units


def solver(immune_units, infect_units):
    """
    Solves the problem of simulating a fight between immune system units and infection units.
    The function performs the following steps:
    1. Simulates a fight between the given immune system units and infection units without any
       boost.
    2. Uses a binary search approach to find the minimum boost required for the immune system
       units to win the fight.
    Args:
        immune_units (list): A list of immune system units.
        infect_units (list): A list of infection units.
    Yields:
        int: The absolute value of the result of the fight without any boost.
        int: The number of remaining immune system units after the fight with the minimum boost
             required for them to win.
    """
    temp_infect_units = [replace(u) for u in infect_units]
    temp_immune_units = [replace(u) for u in immune_units]
    yield abs(fight(temp_immune_units, temp_infect_units))

    l = 0
    r = 10_000
    score = 0
    while r - l > 1:
        boost = (l + r) // 2
        temp_infect_units = [replace(u) for u in infect_units]
        temp_immune_units = [replace(u) for u in immune_units]
        for u in temp_immune_units:
            u.damage += boost
        n_immune_units = fight(temp_immune_units, temp_infect_units)
        if n_immune_units > 0:
            score = n_immune_units
            r = boost
        else:
            l = boost
    yield score


def fight(immune_units, infect_units):
    """
    Simulates a fight between immune system units and infection units until one side is completely
    defeated.
    Args:
        immune_units (list): A list of units belonging to the immune system.
        infect_units (list): A list of units belonging to the infection.
    Returns:
        int: The difference in the total number of units remaining between the immune system and 
             the infection.
             Positive if immune system wins, negative if infection wins, and zero if it's a draw.
    """
    while immune_units != [] and infect_units != []:
        selected_targets = {}
        for unit in attack_order(immune_units + infect_units):
            if unit in immune_units:
                targets = infect_units
            else:
                targets = immune_units
            selected_targets[unit.initiative] = select_target(unit, targets, selected_targets)

        total_kills = 0
        for unit in sorted(immune_units + infect_units, key = lambda u : - u.initiative):
            target = selected_targets[unit.initiative]
            if (target is None) or (unit.attack_type in target.immunities):
                continue
            if unit.attack_type in target.weakness:
                kills = 2 * unit.effective_power // target.hp
            else:
                kills = unit.effective_power // target.hp

            kills = min(kills, selected_targets[unit.initiative].size)
            selected_targets[unit.initiative].size -= kills
            total_kills += kills

        immune_units = [u for u in immune_units if u.size > 0]
        infect_units = [u for u in infect_units if u.size > 0]
        if total_kills == 0:
            return 0
    return sum(u.size for u in immune_units) - sum(u.size for u in infect_units)


def select_target(unit, targets, selected_targets):
    """
    Selects the most optimal target for a given unit from a list of potential targets.
    Args:
        unit: The unit that is selecting a target. This unit should have attributes such as 
              `attack_type`, `effective_power`, and `initiative`.
        targets: A list of potential target units. Each target should have attributes such as 
                 `immunities`, `weakness`, `effective_power`, and `initiative`.
        selected_targets: A dictionary of already selected targets, where the keys are units 
                          and the values are their selected targets.
    Returns:
        The most optimal target unit based on the following criteria:
        1. The target is not already selected by another unit.
        2. The target is not immune to the unit's attack type.
        3. The target is weak to the unit's attack type (higher priority).
        4. The target has the highest effective power (secondary priority).
        5. The target has the highest initiative (tertiary priority).
        If no suitable target is found, returns None.
    """
    return max([target for target in targets if
                    (target not in selected_targets.values() and
                    unit.attack_type not in target.immunities)],
                key = lambda target, unit=unit:
                    (unit.attack_type in target.weakness,
                    target.effective_power,
                    target.initiative),
                default=None)


def attack_order(units):
    """
    Determines the order of attacks based on the effective power and initiative of each unit.
    Args:
        units (list): A list of unit objects, where each unit has attributes 'effective_power' and
        'initiative'.
    Returns:
        list: A list of units sorted by their effective power and initiative in descending order.
    """
    return sorted(units,
                  key = lambda u: (u.effective_power, u.initiative),
                  reverse = True)


def extract_groups(units):
    """
    Extracts and parses group information from a given string of unit descriptions.
    Args:
        units (str): A multiline string where each line describes a unit group. The first line is 
        ignored.
    Returns:
        list: A list of Unit objects, each representing a group with attributes such as quantity, 
        hit points, 
              attack damage, attack type, initiative, weaknesses, and immunities.
    The expected format for each unit description line is:
        "{qty} units each with {hp} hit points {extra} with an attack that does {ad} {at} damage at
        initiative {init}"
        - qty (int): Number of units in the group.
        - hp (int): Hit points for each unit.
        - extra (str): Additional information about weaknesses and immunities, enclosed in 
          parentheses.
        - ad (int): Attack damage.
        - at (str): Attack type.
        - init (int): Initiative value.
    Example:
        units = '''
        10 units each with 100 hit points (weak to fire; immune to cold) with an attack that does
        20 slashing damage at initiative 5
        5 units each with 50 hit points with an attack that does 10 bludgeoning damage at 
        initiative 10
        '''
        groups = extract_groups(units)
    """

    groups = []
    for unit in units.splitlines()[1:]:
        wkns = []
        immt = []
        pattern = "{:d} units each with {:d} hit points{}with an attack that does {:d} {} damage at initiative {:d}"
        qty, hp, extra, ad, at, init = parse(pattern, unit)
        if extra != ' ':
            extra = [item.split(' to ') for item in extra[2:-2].split('; ')]
            for a, l in extra:
                if a == "weak":
                    wkns = l.split(', ')
                else:
                    immt = l.split(', ')
        groups.append(Unit(qty, hp, ad, at, init, wkns, immt))
    return groups
