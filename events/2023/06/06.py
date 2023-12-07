from re     import findall
from numpy  import prod, roots

def preprocessing(input):
    time, distance = input.splitlines()

    time = findall(r'[0-9]+', time)
    time.append(''.join(t for t in time))
    time = (int(t) for t in time)

    distance = findall(r'[0-9]+', distance)
    distance.append(''.join(d for d in distance))
    distance = (int(d) for d in distance)

    ways = []
    for time, distance in zip(time, distance):
        l, h = sorted((int(n) for n in roots([1, - time, distance])))
        ways.append(h - l)
    return ways


def solver(ways):
    yield (2, ways.pop())
    yield (1, prod(ways))
