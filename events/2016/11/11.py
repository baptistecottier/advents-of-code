
def preprocessing(input_):
    return [floor.count('microchip') + floor.count('generator') for floor in input_.splitlines()]

def solver(objects):
    print(objects)
    yield get_moves(objects)

    objects[0] += 4
    yield move(objects)

def move(objects): 
    return sum(2 * sum(objects[:x]) - 3 for x in range(1, 4))

def get_moves(items):
    """
    Through playing around with bolts and nuts,
    I came across the optimal strategy, move things up a floor at a time

    I also discovered to move n items up 1 floor,
        it requires 2 * (n - 1) - 1 moves

    So assuming a "good" start state, it doesn't matter what is on what floor
    Just the number of things per floor
    """
    moves = 0
    while items[-1] != sum(items):
        # print moves, items
        lowest_floor = 0
        while items[lowest_floor] == 0:
            lowest_floor += 1
        moves += 2 * (items[lowest_floor] - 1) - 1
        items[lowest_floor + 1] += items[lowest_floor]
        items[lowest_floor] = 0
    return moves