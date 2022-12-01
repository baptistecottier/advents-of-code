from itertools import count
from AoC_tools import read_input

programs = read_input().splitlines()
programs = [list(map(int,program.split(' <-> ')[1].split(', '))) for program in programs]

size=len(programs)
srtd=[]
grp=0
while len(srtd)<2000:
    cmpt=min([x for x in range(2000) if x not in srtd])
    linked=[cmpt]
    redo=1
    while redo==1:
        redo=0
        for i in range(len(programs)) :
            if i in linked  and any([p not in linked for p in programs[i]]): 
                linked += programs[i]
                redo=1
    linked=sorted(list(set(linked)))
    srtd+=linked
    grp+=1
print(grp)
print(linked)
print(len(linked))