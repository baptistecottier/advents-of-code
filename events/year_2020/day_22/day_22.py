"""
Advent of Code - Year 2020 - Day 22
https://adventofcode.com/2020/day/22
"""

from collections.abc import Iterator
from copy import deepcopy


def preprocessing(puzzle_input: str) -> dict[int, list[int]]:
    """
    Parses the input string into a dictionary mapping player numbers to their list of card values.
    """
    cards = {}
    for n, plain_cards in enumerate(puzzle_input.split('\n\n')):
        cards[n + 1] = list(map(int, plain_cards.splitlines()[1:]))
    return cards


def solver(cards: dict[int, list[int]]) -> Iterator[int]:
    """
    Yields the winner's score for a card game simulation with and without recursion, given the
    initial cards for each player.
    """
    for recursivity in [False, True]:
        yield get_winner_score(deepcopy(cards), recursivity)


def get_winner_score(cards: dict[int, list[int]], recursivity) -> int:
    """
    Calculates and returns the winner's score after playing a card game, optionally using recursive
    rules.
    """
    winner = play_game(cards, recursivity)
    return sum((n + 1) * c for n, c in enumerate(cards[winner][::-1]))


def play_game(cards: dict[int, list[int]], recursivity: bool) -> int:
    """
    Simulates a two-player card game with optional recursion and returns the winning player's
    number.
    """
    decks = []
    winner = -1
    while [] not in cards.values():
        if list(cards.values()) in decks:
            return 1
        decks.append([cards[1], cards[2]])
        a = cards[1].pop(0)
        b, cards[2] = cards[2][0], cards[2][1:]
        if recursivity and a <= len(cards[1]) and b <= len(cards[2]):
            winner = play_game({1: cards[1][:a], 2: cards[2][:b]}, recursivity)
        else:
            if a > b:
                winner = 1
            else:
                winner = 2
        if winner == 1:
            cards[1] += [a, b]
        else:
            cards[2] += [b, a]
    return winner
