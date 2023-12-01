from math import log

preprocessing = int

def solver(nb_players):
    yield play_game(nb_players, 2)
    yield play_game(nb_players, 3)

def play_game(nb_players, base):
    logn   = int(log(nb_players, base))
    winner = nb_players % (base ** logn)
    if base - 1 < nb_players / (base ** logn) < base: 
        winner += base ** ((base - 2) * logn) + winner
    return winner