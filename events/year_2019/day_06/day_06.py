"""
Advent of Code - Year 2019 - Day 6
https://adventofcode.com/2019/day/6
"""

from itertools import product


def preprocessing(puzzle_input: str) -> dict[str, str]:
    """
    Parses a puzzle input string representing orbital relationships into a dictionary mapping each
    object to its direct center.
    """
    orbits: dict[str, str] = {}
    for orbit in puzzle_input.splitlines():
        ctr, pnt = orbit.split(')')
        orbits[pnt] = ctr
    return orbits


def solver(orbits: dict[str, str]) -> tuple[int, int]:
    """
    Calculates the total number of direct and indirect orbits and the minimum orbital transfers
    required between 'YOU' and 'SAN' from a given orbit map.
    """
    paths: list[list[str]] = map_orbits(orbits)
    total_orbits = 0
    you_to_san = 0
    for planet in orbits.keys():
        for path in paths:
            if not you_to_san and 'YOU' in path:
                for dst, p in product(paths, path[::-1]):
                    if {'SAN', p} <= set(dst):
                        you_to_p = path.index('YOU') - path.index(p) - 1
                        p_to_san = dst.index('SAN') - dst.index(p) - 1
                        you_to_san = you_to_p + p_to_san
                        break
            if planet in path:
                total_orbits += path.index(planet)
                break
    if not you_to_san:
        raise ValueError("No path from YOU to SAN")
    return total_orbits, you_to_san


def map_orbits(orbits: dict[str, str]) -> list[list[str]]:
    """
    Generates a list of paths from each orbiting object that does not appear as a center to the
    'COM' (center of mass) in the given orbit map.
    """
    paths: list[list[str]] = []
    for end in orbits:
        if end in orbits.values():
            continue

        path = [end]
        src = orbits[end]
        while src != 'COM':
            path.append(src)
            src = orbits[src]
        path.append('COM')
        paths.append(path[::-1])

    return paths
