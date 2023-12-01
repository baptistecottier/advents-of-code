from pythonfw.classes import Point


def preprocessing(input_):
    return input_.split(',')


def solver(directions):
    path = list()
    pos  = Point()
    
    for step in directions:
        match step:
            case 'nw': pos.move(-1, 0 )
            case 'n' : pos.move(0 , 1 )
            case 'ne': pos.move(1 , 1 )
            case 'se': pos.move(1 , 0 )
            case 's' : pos.move(0 , -1)
            case 'sw': pos.move(-1, -1)
        path.append(pos.manhattan())
        
    yield path[-1]
    yield max(path)