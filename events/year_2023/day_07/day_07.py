"""
Advent of Code - Year 2023 - Day 7
https://adventofcode.com/2023/day/7
"""

from collections import Counter
from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[tuple[str, int]]:
    """
    Parses the puzzle input into a list of tuples containing card strings and their corresponding
    bet amounts.
    """
    bets = [(cards, int(bet)) for cards, bet in
            (hand.split() for hand in puzzle_input.splitlines())]
    return bets


def solver(bets: list[tuple[str, int]]) -> Iterator[int]:
    """
    Yields the winnings for a variant with no joker and one with 'J' as joker.
    """
    for joker in '_J':
        yield winnings(bets, joker)


def winnings(bets: list[tuple[str, int]], joker: str):
    """
    Calculates the total winnings based on ranked poker hands with a specified joker card.
    """
    hand_sort = []
    card_strength = {
        card:
            strength for strength, card in enumerate(joker + "23456789TJQKA".replace(joker, ''))}

    for cards, bet in bets:
        jokers = cards.count(joker)
        jcards = cards.replace(joker, '')

        hand_strength = sorted(Counter(jcards).values(), reverse=True)
        hand_strength += [0 for _ in range(5 - len(hand_strength))]
        hand_strength[0] = min(5, hand_strength[0] + jokers)

        cards_strength = [card_strength[card] for card in cards]
        hand_sort.append((hand_strength, cards_strength, bet))

    return sum(n * b for n, (_, _, b) in enumerate(sorted(hand_sort), 1))
