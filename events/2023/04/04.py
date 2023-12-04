def preprocessing(input):
    scores = []
    for game in input.splitlines():
        draw, card = game.split(' | ')
        draw = [int(n) for n in draw.split()[2:]]
        card = [int(n) for n in card.split()]
        score = len([n for n in card if n in draw])
        scores.append(score)
    return scores

def solver(scores):
    points = 0
    scratch = {n: 1 for n in range(len(scores))}
    for game, score in enumerate(scores):
        if score > 0: 
            for gg in range(game + 1, game + score + 1):
                scratch[gg] += scratch[game]
            points += pow(2, score - 1)
    yield points
    yield sum(scratch.values())