def generator(input): 
    directions = []
    for direction in input:
        if direction == '(': directions.insert(0, 1)
        else: directions.insert(0, -1)
    return directions

def part_1(directions): 
    return sum(directions)

def part_2(directions): 
    floor, initial_length = 0, len(directions)
    while floor >= 0: 
        floor += directions.pop()
    return initial_length - len(directions)
       