with open("Day10/input") as f:
    instructions=f.read().splitlines()
    c_open=['(','{','[','<']
    c_close=[')','}',']','>']
    syntax_error=[]
    corrupted=[]
    for instruction in instructions:
        next_to_close=[instruction[0]]
        i=1
        while(i<len(instruction)):
            if  len(next_to_close)==0 or instruction[i]!=c_close[c_open.index(next_to_close[-1])]:
                if instruction[i] in c_open : next_to_close.append(instruction[i])
                else : 
                    syntax_error.append(instruction[i])
                    corrupted.append(instruction)
                    break

            else : next_to_close=next_to_close[:-1]
            i+=1
    score=0
    for e in syntax_error:
        if e==')' : score += 3
        if e==']' : score += 57
        if e=='}' : score += 1197
        if e=='>' : score += 25137
print("Part I:", score)

incomplete_instructions=[item for item in instructions if item not in corrupted]

map={'(':'1','[' : '2' , '{':'3', '<' : '4'}
scores=[]
for instruction in incomplete_instructions:
    next_to_close=[instruction[0]]
    i=1
    while(i<len(instruction)):
        if  len(next_to_close)==0 or instruction[i]!=c_close[c_open.index(next_to_close[-1])]:
            if instruction[i] in c_open : next_to_close.append(instruction[i])
        else : next_to_close=next_to_close[:-1]
        i+=1
    base5=''.join(map[item] for item in reversed(next_to_close))
    scores.append(int(base5,5))
scores.sort()
print(scores[(len(scores)-1)//2])