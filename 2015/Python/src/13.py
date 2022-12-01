import itertools

with open("Day13/input.txt") as f:
    criterions=f.read().splitlines()
    attendees=list(set([item.split(' ')[0] for item in criterions]))+['Me']
    print(attendees)
    happiness=[[0 for x in range(len(attendees))] for y in range(len(attendees))]
    for criterion in criterions:
        words=criterion.replace('.','').split(' ')
        happiness[attendees.index(words[0])][attendees.index(words[-1])]=(-1+2*(words[2]=='gain')) * int(words[3])
    print(happiness)

    max_happiness=0
    for arrangement in list(itertools.permutations(attendees)):
        arrangement=list(arrangement)
        happy_rate=sum([happiness[attendees.index(arrangement[i])][attendees.index(arrangement[(i+1)%len(attendees)])] for i in range(len(arrangement))]) + sum([happiness[attendees.index(arrangement[(i+1)%len(attendees)])][attendees.index(arrangement[(i)%len(attendees)])] for i in range(len(arrangement))])
        max_happiness=max(max_happiness,happy_rate)
    print(max_happiness)