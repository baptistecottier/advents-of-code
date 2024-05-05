def preprocessing(puzzle_input):
    shuffle = []
    for task in puzzle_input.splitlines():
        if "cut" in task:
            shuffle.append(("cut", int(task[4:])))
        elif "inc" in task:
            shuffle.append(("inc", int(task[19:])))
        else : 
            shuffle.append(("rev", 0))
    return shuffle

def deal(deck):
    return deck[::-1]

def cut(deck, n):
    a, b = deck[:n], deck[n:]
    return b + a

def inc(deck, n):
    l = len(deck)
    deck2 = [0 for _ in range(l)]
    for k in range(l):
        deck2[(k * n) % l] = deck.pop(0)
    return deck2


def solver(shuffle):
    deck = [x for x in range(10007)]
    for f, n in shuffle:
        match f:
            case "cut": deck = cut(deck, n)
            case "inc": deck = inc(deck, n)
            case "rev": deck = deal(deck)
    yield deck.index(2019)