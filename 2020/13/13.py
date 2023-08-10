from pythonfw.functions import chinese_remainder

def preprocessing(input): 
    details   = input.splitlines()
    timestamp = int(details[0])
    bus       = (int(item) for item in details[1].replace('x','0').split(','))
    return timestamp, bus

def solver(input):
    pairs = set()
    times = dict()
    timestamp, bus = input
    for (n, id) in enumerate(input[1]):
        if id != 0:
            times[-timestamp % id] = id * (-timestamp % id)
            pairs.add((-n, id))
    yield times[min(times.keys())]
    yield (2, chinese_remainder(pairs))