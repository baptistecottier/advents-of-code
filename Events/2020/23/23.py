def preprocessing(input_): 
    return [int(item) -1 for item in input_]

def move(cups, steps):
    next    = dict(zip(cups, cups[1:] + [cups[0]]))
    bound   = len(cups)
    current = cups[0]

    for _ in range(steps):
        dest = (current - 1) % bound
        while dest in (a:= next[current], b := next[a], c:= next[b]):
            dest = (dest - 1) % bound
            
        next[current] = next[c]
        next[c]       = next[dest]
        next[dest]    = a
        current       = next[current]
    return next


def solver(cups):
    next   = move(cups, 100)
    curr   = 0
    answer = ""
    while next[curr]: answer += str((curr:= next[curr]) + 1)
    yield answer

    cups += list(range(max(cups) + 1, 1_000_000))
    next = move(cups, 10_000_000)
    yield (next[0] + 1) * (next[next[0]] + 1)