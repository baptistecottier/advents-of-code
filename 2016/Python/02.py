with open("inputs/02.txt") as f:
    numbers=f.read().splitlines()

position=5 # Starting point is the key number 5
code='' # Initialize the code at 0

for number in numbers : # We set each code values
    for instruction in list(number) : # By wandering the instructions
        if instruction == 'D' and 1 <= position <= 6 : position+=3
        if instruction == 'U' and 4 <= position <= 9 : position-=3
        if instruction == 'L' and position % 3 != 1 : position-=1
        if instruction == 'R' and position % 3 != 0 : position+=1
        
    code+=str(position) # We have a new code value, add it

print("If my math is correct, the code should be", (code) + '.')


# Same thing with the new keypad
position=5
code=''

for number in numbers : 
    for instruction in list(number) : 
        if instruction == 'D' : 
            if position in [1,11] : position+=2
            elif position in [2,3,4,6,7,8] : position+=4

        elif instruction == 'U' : 
            if position in [3,13] : position-=2
            elif position in [6,7,8,10,11,12] : position-=4

        elif instruction == 'L' and position not in [1, 2, 5, 10, 13] : position-=1
        elif instruction == 'R' and position not in [1, 4, 9, 12, 13] : position+=1

    code+=format(position,'X')
print("Oops, keypad is a bit stranger that I thought. Now, the code should be", code)