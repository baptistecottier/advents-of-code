
from itertools          import product
from pythonfw.functions import dijkstra
def preprocessing(input):
    risk_map = {}
    for y, row in enumerate(input.splitlines()):
        for x, risk in enumerate(row):
            risk_map[(x, y)] = int(risk)
    return (risk_map, (x, y))

def solver(input): 
    map_dict, (w, h) = input
    yield dijkstra(map_dict, (w, h))
    for (x, y), risk in list(map_dict.items()):
        for kx, ky in product(range(5), repeat=2):
            map_dict[(x + kx * (w + 1), y + ky * (h + 1))] = 1 + ((risk + kx + ky - 1) % 9)
    yield dijkstra(map_dict, (5 * (w + 1) - 1, 5 * (h + 1) - 1))



