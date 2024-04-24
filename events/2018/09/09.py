from codecs import latin_1_decode
from collections import defaultdict, deque

def preprocessing(puzzle_input):
    details = puzzle_input.split(' ')
    return (int(details[0]), int(details[-2]))

def solver(players, last_marble):
    
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, 100 * last_marble + 1):
        if marble == last_marble + 1: yield max(scores.values())
        
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    yield max(scores.values())

