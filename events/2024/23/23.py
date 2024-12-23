from collections import defaultdict, deque
from itertools   import combinations

def preprocessing(puzzle_input):
    computers = set()
    connections = defaultdict(set)
    for connection in puzzle_input.splitlines():
        a, b = connection.split('-')
        connections[a].add(b)
        connections[b].add(a)
        computers.update({a, b})
    return computers, connections

def solver(computers, connections):
    suspected_LANs = 0
    for a, b, c in combinations(computers, 3):
        if b in connections[a] and c in connections[a] and b in connections[c]:
            if any(n.startswith('t') for n in (a, b, c)):
                suspected_LANs += 1
    yield suspected_LANs
    
    queue = deque([[c] for c in computers])
    while len(queue) > 1:
        lan = queue.popleft()
        for c in computers:
            if c not in lan:
                if all(b in connections[c] for b in lan):
                    queue.append(lan + [c])
                    break
    yield ",".join(sorted(queue.pop()))