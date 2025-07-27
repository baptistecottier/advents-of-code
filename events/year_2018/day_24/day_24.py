"""
Advent of Code - Year 2018 - Day 24
https://adventofcode.com/2018/day/24
"""

# Standard imports
from collections.abc import Iterator
from dataclasses import dataclass, replace

# Third-party import
from parse import parse, Result


@dataclass(unsafe_hash=True)
class Unit:
    """
    Represents a unit group with combat statistics and special attributes.
    """
    size: int
    hp: int
    damage: int
    attack_type: str
    initiative: int
    weakness: list[str]
    immunities: list[str]

    @property
    def effective_power(self):
        """Calculate the effective power by multiplying group size and damage."""
        return self.size * self.damage


def preprocessing(puzzle_input: str) -> tuple[list[Unit], list[Unit]]:
    """
    Parses puzzle input to extract immune system and infection groups.
    """
    immune, infect = puzzle_input.split("\n\n")
    immune_units = extract_groups(immune)
    infect_units = extract_groups(infect)
    return immune_units, infect_units


def solver(immune_units: list[Unit], infect_units: list[Unit]) -> Iterator[int]:
    """
    Solves the immune system vs infection battle by first simulating without boost, then finding
    minimum boost needed for immune system victory using binary search.
    """
    temp_infect_units = [replace(u) for u in infect_units]
    temp_immune_units = [replace(u) for u in immune_units]
    yield abs(fight(temp_immune_units, temp_infect_units))

    low = 0
    up = 10_000
    score = 0
    while up - low > 1:
        boost = (low + up) // 2
        temp_infect_units = [replace(u) for u in infect_units]
        temp_immune_units = [replace(u) for u in immune_units]

        for u in temp_immune_units:
            u.damage += boost
        n_immune_units = fight(temp_immune_units, temp_infect_units)

        if n_immune_units > 0:
            score = n_immune_units
            up = boost
        else:
            low = boost

    yield score


def fight(immune_units: list[Unit], infect_units: list[Unit]) -> int:
    """
    Simulates combat between immune system and infection units, returning the net unit difference.
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
        for unit in sorted(immune_units + infect_units, key=lambda u: - u.initiative):
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


def select_target(
        unit: Unit, targets: list[Unit], selected_targets: dict[int, Unit | None]
        ) -> Unit | None:
    """
    Select the best target for a unit to attack based on weakness, effective power, and initiative
    priority.
    """
    return max(
        (target for target in targets if (
            target not in selected_targets.values() and
            unit.attack_type not in target.immunities)),
        key=lambda target, unit=unit: (
            unit.attack_type in target.weakness,
            target.effective_power,
            target.initiative),
        default=None)


def attack_order(units: list[Unit]) -> list[Unit]:
    """
    Determines the order of attacks based on the effective power and initiative of each unit.
    Args:
        units (list): A list of unit objects, where each unit has attributes 'effective_power' and
        'initiative'.
    Returns:
        list: A list of units sorted by their effective power and initiative in descending order.
    """
    return sorted(
        units,
        key=lambda u: (u.effective_power, u.initiative),
        reverse=True)


def extract_groups(units: str) -> list[Unit]:
    """
    Parse unit descriptions from a multi-line string and return Unit objects.

    Args:
        units (str): Multi-line string with header and unit descriptions containing
                    combat stats and optional weaknesses/immunities in parentheses.

    Returns:
        list[Unit]: List of parsed Unit objects with combat statistics.

    Raises:
        ValueError: If input doesn't match expected format.
    """
    groups = []
    for unit in units.splitlines()[1:]:
        wkns = []
        immt = []
        pattern = ("{:d} units each with {:d} hit points{}with an attack that does {:d} {} damage "
                   "at initiative {:d}")
        result = parse(pattern, unit)
        if isinstance(result, Result):
            qty, hp, extra, ad, at, init = result
        else:
            raise ValueError("Input does not match with pattern")
        if extra != ' ':
            extra = [item.split(' to ') for item in extra[2:-2].split('; ')]
            for a, l in extra:
                if a == "weak":
                    wkns = l.split(', ')
                else:
                    immt = l.split(', ')
        groups.append(Unit(qty, hp, ad, at, init, wkns, immt))
    return groups
