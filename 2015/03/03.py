def generator(input):
    directions = []
    for house in input:
        match house:
            case '^': directions.append((0,1))
            case '>': directions.append((1,0))
            case 'v': directions.append((0,-1))
            case '<': directions.append((-1, 0))
    return directions

def part_1(directions):
    santa_x, santa_y = 0, 0
    houses = {(0, 0)}
    for (santa_dx, santa_dy) in directions:
        santa_x, santa_y = santa_x + santa_dx, santa_y + santa_dy
        if (santa_x, santa_y) not in houses: houses.add((santa_x, santa_y))
    return len(houses)
        
def part_2(directions):
    houses = {(0, 0)}
    directions = zip(directions[::2], directions[1::2])
    santa_x, santa_y = 0, 0
    robot_x, robot_y = 0, 0
    for (santa_dx, santa_dy), (robot_dx, robot_dy) in directions:
        santa_x, santa_y = santa_x + santa_dx, santa_y + santa_dy
        robot_x, robot_y = robot_x + robot_dx, robot_y + robot_dy
        if (santa_x, santa_y) not in houses: houses.add((santa_x, santa_y))
        if (robot_x, robot_y) not in houses: houses.add((robot_x, robot_y))
    return len(houses)