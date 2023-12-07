from collections import Counter

def preprocessing(input): 
    bets = [(cards, int(bet)) for cards, bet in (hand.split() for hand in input.splitlines())]
    return bets

def solver(bets): 
    yield winnings(bets)    
    yield winnings(bets, jkr = 'J')

def winnings(bets, jkr = '_'): 
    hand_sort = []
    card_strength = jkr + "23456789TJQKA".replace(jkr, '')
    
    for cards, bet in bets: 
        jokers = cards.count(jkr)
        jcards = cards.replace(jkr, '')

        cnts = sorted(Counter(jcards).values(), reverse=True)
        cnts += [0 for _ in range(5 - len(cnts))]        

        i = 0
        while jokers > 0:
            if cnts[i] < 5:
                cnts[i] += 1
                jokers -= 1
            else : i += 1

        hand_strength = list(Counter(cnts).items())
        cards_strength = [card_strength.index(card) for card in cards]

        hand_sort.append((hand_strength, cards_strength, bet))
 
    hand_sort = sorted(hand_sort)
    return sum(n * b for  n, (_, _, b) in enumerate(hand_sort, 1))