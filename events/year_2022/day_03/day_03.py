"""
Advent of Code - Year 2022 - Day 3
https://adventofcode.com/2022/day/3
"""


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Splits the input puzzle string into a list of lines.
    """
    return puzzle_input.splitlines()


def solver(rucksacks: list[str]) -> tuple[int, int]:
    """
    Calculates the sum of item and badge priorities for groups of rucksacks based on character
    intersections.
    """
    priorites = {c: ord(c) - 96 for c in 'abcdefghijklmonpqrstuvwxyz'}
    priorites.update({c: ord(c) - 38 for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'})
    items_priority = 0
    badges_priority = 0

    for ga, gb, gc in (rucksacks[n: n + 3] for n in range(0, len(rucksacks), 3)):
        for sack in (ga, gb, gc):
            item = set(sack[:len(sack) // 2]).intersection(set(sack[len(sack) // 2:])).pop()
            items_priority += priorites[item]
        badge = set(ga).intersection(set(gb)).intersection(set(gc)).pop()
        badges_priority += priorites[badge]

    return items_priority, badges_priority
