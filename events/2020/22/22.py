from copy import deepcopy


def preprocessing(puzzle_input):
    cards = {}
    for n, plain_cards in enumerate(puzzle_input.split('\n\n')):
        cards[n + 1] = [int(card) for card in plain_cards.splitlines()[1:]]
    return cards

def solver(cards):
    yield part_1(deepcopy(cards))
    yield part_2(cards)

def part_1(puzzle_input): 
    cards = puzzle_input
    while [] not in cards.values():
        a, cards[1] = cards[1][0], cards[1][1:]
        b, cards[2] = cards[2][0], cards[2][1:]
        if a > b : cards[1] += [a, b]
        else: cards[2] += [b, a]
    if cards[1] == []: winner = 2
    else: winner = 1
    return sum((n + 1) * c for n, c in enumerate(cards[winner][::-1]))

def part_2(puzzle_input): 
    cards = puzzle_input
    decks = []
    while [] not in cards.values():
        if list(cards.values()) in decks:
            return 1
        else:
            decks.append([cards[1], cards[2]])
            a, cards[1] = cards[1][0], cards[1][1:]
            b, cards[2] = cards[2][0], cards[2][1:]
            if a <= len(cards[1]) and b <= len(cards[2]):
                winner = recursive_play({1: cards[1][:a], 2:cards[2][:b]})
            else: 
                if a > b: winner = 1
                else: winner = 2
            if winner == 1 : cards[1] += [a, b]
            else: cards[2] += [b, a]
    if cards[1] == []: winner = 2
    else: winner = 1
    return sum((n + 1) * c for n, c in enumerate(cards[winner][::-1]))

def recursive_play(cards):
    decks = []
    while [] not in cards.values():
        if list(cards.values()) in decks:
            return 1
        else:
            decks.append([cards[1], cards[2]])
            a, cards[1] = cards[1][0], cards[1][1:]
            b, cards[2] = cards[2][0], cards[2][1:]
            if a <= len(cards[1]) and b <= len(cards[2]):
                winner = recursive_play({1: cards[1][:a], 2:cards[2][:b]})
            else: 
                if a > b: winner = 1
                else: winner = 2
            if winner == 1 : cards[1] += [a, b]
            else: cards[2] += [b, a]
    return winner
