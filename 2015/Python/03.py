def generator(input) :
    directions = []
    for house in input :
        match house :
            case '^' : directions.append((0,1))
            case '>' : directions.append((1,0))
            case 'v' : directions.append((0,-1))
            case '<' : directions.append((-1, 0))
    return directions

def part_1(directions) :
    position = [0,0]
    houses = [[0,0]]
    for (dx, dy) in directions :
        position[0] += dx
        position[1] += dy
        if position not in houses : houses.append(position.copy())
    return len(houses)
        
def part_2(directions) :
    houses = [[0,0]]
    positions = [[0,0],[0,0]]
    for i in range(len(directions)) :
        (dx, dy) = directions[i]
        positions[i%2][0] += dx
        positions[i%2][1] += dy
        if positions[i%2] not in houses : houses.append(positions[i%2].copy())
    return len(houses)