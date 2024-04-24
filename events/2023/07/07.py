from collections import Counter

def preprocessing(puzzle_input): 
    bets = [(cards, int(bet)) for cards, bet in (hand.split() for hand in puzzle_input.splitlines())]
    return bets

def solver(bets): 
    yield winnings(bets)    
    yield winnings(bets, joker = 'J')

def winnings(bets, joker = '∅'): 
    hand_sort = []
    card_strength = {card: strength for strength, card in enumerate(joker + "23456789TJQKA".replace(joker, ''))}
    
    for cards, bet in bets: 
        jokers = cards.count(joker)
        jcards = cards.replace(joker, '')

        hand_strength = sorted(Counter(jcards).values(), reverse=True)
        hand_strength += [0 for _ in range(5 - len(hand_strength))]        
        hand_strength[0] = min(5, hand_strength[0] + jokers)

        cards_strength = [card_strength[card] for card in cards]
        hand_sort.append((hand_strength, cards_strength, bet))
 
    return sum(n * b for  n, (_, _, b) in enumerate(sorted(hand_sort), 1))