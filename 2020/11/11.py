from copy import deepcopy

def preprocessing(input):
    rows = input.splitlines()
    l = len(rows)
    w = len(rows[0])
    seats = [[0 for _ in range (w + 2)] for _ in range(l + 2)]
    for r in range(1,l + 1):
        for c in range(1,w + 1):
            seats[r][c] = int(rows[r-1][c-1] == 'L')
    return seats

def solver(input):
    boat = input
    updated_boat = apply_rules(boat)
    while boat != updated_boat:
        boat = deepcopy(updated_boat)
        updated_boat = apply_rules(boat)
    yield sum(sum(seat == 2 for seat in row) for row in updated_boat)

    boat = input
    updated_boat = apply_rules(boat, False)
    while boat != updated_boat:
        boat = deepcopy(updated_boat)
        updated_boat = apply_rules(boat, False)
    yield sum(sum(seat == 2 for seat in row) for row in updated_boat)

def apply_rules(boat, adjacent = True):
    updated_boat = deepcopy(boat)
    for r in range(1,len(boat)):
        for c in range(1, len(boat[0])):
            neighbours = []
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                rr = r + dr
                cc = c + dc
                if not adjacent: 
                    while rr in range(len(boat)) and cc in range(len(boat[0])) and boat[rr][cc] == 0: 
                        rr += dr
                        cc += dc
                if rr in range(len(boat)) and cc in range(len(boat[0])): neighbours.append((rr,cc))
            match boat[r][c]:
                case 1: 
                    if all(boat[rr][cc] in [0, 1] for rr, cc in neighbours):
                        updated_boat[r][c] = 2
                case 2: 
                    if sum(boat[rr][cc] == 2 for rr, cc in neighbours) >= (5 - adjacent):
                        updated_boat[r][c] = 1

    return updated_boat