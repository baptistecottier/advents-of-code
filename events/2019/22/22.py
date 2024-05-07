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

def deal(nb_cards, pos):
    return nb_cards - pos - 1

def cut(nb_cards, n, pos):
    return (pos - n) % nb_cards

def rev_cut(nb_cards, n, pos):
    return (pos + n) % nb_cards

def inc(nb_cards, n, pos):
    return (pos * n) % nb_cards

def rev_inc(nb_cards, n, pos):
    return (pos * pow(n, -1, nb_cards)) % nb_cards

def solver(shuffle):
    yield proceed(shuffle, 10_007, 2019)
    yield rev_proceed(shuffle, 119315717514047, 2020, 101741582076661)


def proceed(shuffle, nb_cards, pos):
    for f, n in shuffle:
        match f:
            case "cut": pos = cut(nb_cards, n, pos)
            case "inc": pos = inc(nb_cards, n, pos)
            case "rev": pos = deal(nb_cards, pos)
    return pos

def rev_proceed(shuffle, nb_cards, index, rep = 1):
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