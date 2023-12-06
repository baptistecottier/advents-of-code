import re
import numpy as np

def preprocessing(input):
    time, distance = input.splitlines()

    time = re.findall(r'[0-9]+', time)
    time.append(''.join(t for t in time))
    time = (int(t) for t in time)

    distance = re.findall(r'[0-9]+', distance)
    distance.append(''.join(d for d in distance))
    distance = (int(d) for d in distance)

    return zip(time, distance)

def solver(input):
    total = 1
    for time, distance in input:
        l, h = sorted((int(n) for n in np.roots([1, - time, distance])))
        total *= (h - l)
    yield total // (h - l)
    yield h - l
