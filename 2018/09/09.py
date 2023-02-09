def generator(input):
    details = input.split(' ')
    return (int(details[0]), int(details[-2]))


def part_1(input): return solver(input)

def part_2(input): return solver((input[0], 100 * input[1]))

def solver(input):
    nb_players, nb_marbles = input
    circle = [0]
    i = 1
    scores = [0 for _ in range(nb_players)]
    for marble in range(1, nb_marbles + 1):
        if marble % ( nb_marbles // 100) == 0 : print(marble // (nb_marbles // 100))
        if marble % 23 == 0 :
            scores[marble % nb_players] += marble
            i = (i - 9) % len(circle)
            k = circle.pop(i)
            scores[marble % nb_players] += k
        else : 
            circle.insert(i ,marble)
        i = (i + 1) % len(circle) + 1
    return max(scores)