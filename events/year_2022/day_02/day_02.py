"""
Advent of Code - Year 2022 - Day 2
https://adventofcode.com/2022/day/2
"""


def preprocessing(puzzle_input: str) -> dict[tuple[int, int], int]:
    """
    Parses the puzzle input into a dictionary counting occurrences of each (adv, me) duel pair.
    """
    duels = {(p, q): 0 for p in range(3) for q in range(1, 4)}
    for duel in puzzle_input.splitlines():
        adv, me = duel.split(' ')
        adv = int(ord(adv)) - 65
        me = int(ord(me)) - 87
        duels[(adv, me)] += 1
    return duels


def solver(duels: dict[tuple[int, int], int]) -> tuple[int, int]:
    """
    Calculates and returns the total and real scores from a dictionary of duels with their
    respective counts.
    """
    total_score = 0
    real_score = 0
    for (adv, me), rep in duels.items():
        total_score += rep * (me + 3 * ((me - adv) % 3))
        real_score += rep * (3 * me - 2 + (me + 1 + adv) % 3)
    return total_score, real_score
