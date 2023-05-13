
from itertools import product

def generator(input):
    risk_map = {}
    for y, row in enumerate(input.splitlines()):
        for x, risk in enumerate(row):
            risk_map[(x, y)] = int(risk)
    return (risk_map, (x, y))

def part_1(input): return dijkstra(*input)

def part_2(input): 
    map_dict, (w, h) = input
    for (x, y), risk in list(map_dict.items()):
        for kx, ky in product(range(5), repeat=2):
            map_dict[(x + kx * (w + 1), y + ky * (h + 1))] = 1 + ((risk + kx + ky - 1) % 9)
    return dijkstra(map_dict, (5 * (w + 1) - 1, 5 * (h + 1) - 1))


def dijkstra(map_dict, end_coords):
    unvisited = set(map_dict.keys())
    node_dict = {(0, 0): 0}
    current_node = (0, 0)
    
    while current_node != end_coords:
        x, y = current_node
        risk = node_dict[current_node]
        
        for next_to in [item for item in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if item in unvisited]:
            
            current_risk = node_dict.get(next_to, None)
            new_risk = risk + map_dict[next_to]
            if not current_risk or new_risk < current_risk:
                node_dict[next_to] = new_risk

        unvisited.remove(current_node)
        del node_dict[current_node]

        lowest_risk = min(node_dict.values())
        for coords, risk in node_dict.items():
            if risk == lowest_risk:
                current_node = coords
                break

    return node_dict[end_coords]
