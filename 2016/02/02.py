def generator(input):
    return input.splitlines()


def part_1(input):
    position=5 
    code=''

    for number in input : 
        for instruction in list(number) : 
            if instruction == 'D'   and position not in [7, 8, 9] : position+=3
            elif instruction == 'U' and position not in [1, 2, 3] : position-=3
            elif instruction == 'L' and position not in [1, 4, 7] : position-=1
            elif instruction == 'R' and position not in [3, 6, 9] : position+=1
            
        code+=str(position) 

    return code


def part_2(input):
    position=5
    code=''

    for number in input : 
        for instruction in list(number) : 
            if instruction == 'D' : 
                if position in [1,11] : position+=2
                elif position in [2,3,4,6,7,8] : position += 4

            elif instruction == 'U' : 
                if position in [3,13] : position-=2
                elif position in [6,7,8,10,11,12] : position-=4

            elif instruction == 'L' and position not in [1, 2, 5, 10, 13] : position-=1
            elif instruction == 'R' and position not in [1, 4, 9, 12, 13] : position+=1

        code+=format(position,'X')
    return code
