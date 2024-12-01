def preprocessing(data):
    return data.splitlines()

def solver(procedure):
    yield squared_keypad(procedure)
    yield diamond_keypad(procedure)
    
def squared_keypad(procedures):
    code = ""
    position = 5 
    for procedure in procedures:
        for instruction in procedure: 
            match instruction, position:
                case ['D', (1| 2| 3| 4| 5| 6)]: position += 3
                case ['U', (4| 5| 6| 7| 8| 9)]: position -= 3
                case ['L', (2| 3| 5| 6| 8| 9)]: position -= 1
                case ['R', (1| 2| 4| 5| 7| 8)]: position += 1
        code += format(position)
    return code

def diamond_keypad(procedures):
    code = ""
    position = 5 
    for procedure in procedures:
        for instruction in procedure: 
            match instruction, position:
                case ['D', (1| 11)]:                    position += 2
                case ['D', (2| 3| 4| 6| 7| 8)]:         position += 4     
                case ['U', (3| 13)]:                    position -= 2
                case ['U', (6| 7| 8| 10| 11| 12)]:      position -= 4
                case ['L', (3| 4| 6| 7| 8| 9| 11| 12)]: position -= 1
                case ['R', (2| 3| 5| 6| 7| 8| 10| 11)]: position += 1
        code += format(position, 'X')
    return code

