from pythonfw.functions import chinese_remainder

def preprocessing(puzzle_input): 
    details   = puzzle_input.splitlines()
    timestamp = int(details[0])
    bus       = (int(item) for item in details[1].replace('x','0').split(','))
    return timestamp, bus

def solver(timestamp, bus):
    pairs = set()
    times = dict()
    for (n, id) in enumerate(bus):
        if id != 0:
            times[-timestamp % id] = id * (-timestamp % id)
            pairs.add((-n, id))
    yield times[min(times.keys())]
    yield chinese_remainder(pairs)