"""
Advent of Code - Year 2018 - Day 2
https://adventofcode.com/2018/day/2
"""


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Splits the puzzle input string into a list of strings, one per line.
    """
    return puzzle_input.splitlines()


def solver(boxids: list[str]) -> tuple[int, str]:
    """
    Solves the box ID checksum problem by computing product of IDs with exactly 2 and 3
    repeated characters, and finding the common letters between two IDs differing by one character.

    Args:
        boxids: List of box ID strings

    Returns:
        tuple: (checksum, common_letters)
            - checksum: Product of count of IDs with exactly 2 and 3 repeated characters
            - common_letters: Common letters between two IDs that differ by exactly one character
    """
    len_id = len(boxids[0])
    twice = 0
    thrice = 0
    common_letters = ""

    for ida in boxids:
        counts = set(ida.count(c) for c in ida)
        if 2 in counts:
            twice += 1

        if 3 in counts:
            thrice += 1

        if common_letters == "":
            for idb in boxids:
                common = list(a for a, b in zip(ida, idb) if a == b)
                if len(common) == len_id - 1:
                    common_letters = ''.join(common)

    return twice * thrice, common_letters
