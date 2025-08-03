"""
Advent of Code - Year 2019 - Day 22
https://adventofcode.com/2019/day/22
"""


def preprocessing(puzzle_input: str) -> list[tuple[str, int]]:
    """
    Parses the input string into a list of shuffle operations represented as (operation, value)
    tuples.
    """
    shuffle = []
    for task in puzzle_input.splitlines():
        if "cut" in task:
            shuffle.append(("cut", int(task[4:])))
        elif "inc" in task:
            shuffle.append(("inc", int(task[19:])))
        else:
            shuffle.append(("rev", 0))
    return shuffle


def deal(nb_cards: int, pos: int) -> int:
    """
    Returns the new position of a card after performing a 'deal into new stack' operation on a deck
    of given size.
    """
    return nb_cards - pos - 1


def cut(nb_cards: int, n: int, pos: int) -> int:
    """
    Returns the new position of a card after performing a cut operation on a deck of cards.
    """
    return (pos - n) % nb_cards


def rev_cut(nb_cards: int, n: int, pos: int) -> int:
    """
    Returns the previous position of a card after performing a 'cut n' operation on a deck of
    nb_cards cards.
    """
    return (pos + n) % nb_cards


def inc(nb_cards: int, n: int, pos: int) -> int:
    """
    Returns the new position of a card after applying an increment shuffle with increment n in a
    deck of nb_cards cards.
    """
    return (pos * n) % nb_cards


def rev_inc(nb_cards: int, n: int, pos: int) -> int:
    """
    Reverses the "deal with increment n" shuffle operation by computing the original position of a
    card in a deck of nb_cards.
    """
    return (pos * pow(n, -1, nb_cards)) % nb_cards


def solver(shuffle: list[tuple[str, int]]) -> tuple[int, int]:
    """
    Solves the card shuffling problem by applying the shuffle instructions and their reverse to
    specified deck sizes and positions.
    """
    return (proceed(shuffle, 10_007, 2019),
            rev_proceed(shuffle, 119315717514047, 2020, 101741582076661))


def proceed(shuffle: list[tuple[str, int]], nb_cards: int, pos: int) -> int:
    """
    Processes a sequence of shuffle operations on a deck of cards and returns the final position of
    a specified card.
    """
    for f, n in shuffle:
        match f:
            case "cut": pos = cut(nb_cards, n, pos)
            case "inc": pos = inc(nb_cards, n, pos)
            case "rev": pos = deal(nb_cards, pos)
    return pos


def rev_proceed(shuffle: list[tuple[str, int]], nb_cards: int, index, rep=1) -> int:
    """
    Computes the final position of a card after applying a sequence of reverse shuffle operations
    multiple times on a deck of cards.
    """
    def rev_once(pos):
        for f, n in shuffle[::-1]:
            match f:
                case "cut": pos = rev_cut(nb_cards, n, pos)
                case "inc": pos = rev_inc(nb_cards, n, pos)
                case "rev": pos = deal(nb_cards, pos)
        return pos

    y = rev_once(0)
    z = rev_once(y)

    a = ((z - y) * pow(y, -1, nb_cards)) % nb_cards

    p = pow(a, rep, nb_cards)
    q = pow(a - 1, -1, nb_cards) * y * (p - 1)

    return (p * index + q) % nb_cards
