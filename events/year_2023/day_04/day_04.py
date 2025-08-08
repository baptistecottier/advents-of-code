"""
Advent of Code - Year 2023 - Day 4
https://adventofcode.com/2023/day/4
"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Parses the puzzle input and returns a list of scores representing the count of matching numbers
    for each game.
    """
    scores = []
    for game in puzzle_input.splitlines():
        draw, card = game.split(' | ')
        draw = [int(n) for n in draw.split()[2:]]
        card = [int(n) for n in card.split()]
        score = len([n for n in card if n in draw])
        scores.append(score)
    return scores


def solver(scores: list[int]) -> tuple[int, int]:
    """
    Calculates total points and the sum of scratch cards based on a list of scores.
    """
    points = 0
    scratch = [1 for _ in range(len(scores))]
    for game, score in enumerate(scores):
        points += (1 << score) >> 1
        for gg in range(game + 1, game + score + 1):
            scratch[gg] += scratch[game]
    return points, sum(scratch)
