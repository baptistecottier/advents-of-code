with open("Day08/input.txt") as f:
    lines=f.read().splitlines()
    length_difference=sum([len(line) - len(eval(line)) for line in lines])
    print('There is a difference of', length_difference, 'characters between the string literals and the value of strings')
    length_difference=0
    for line in lines : 
        length_difference+=2+(line.count('\"'))
        length_difference+=(line.count('\\'))
    print('Going the other way, the newly encoded strings have', length_difference,'more characters thant the original string')