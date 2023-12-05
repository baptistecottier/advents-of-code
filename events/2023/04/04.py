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
    scratch = [1 for _ in range(len(scores))]
    for game, score in enumerate(scores):
        points += (1 << score) >> 1
        for gg in range(game + 1, game + score + 1):
            scratch[gg] += scratch[game]
    yield points
    yield sum(scratch)