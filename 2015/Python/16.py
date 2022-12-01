with open("input.txt") as f:
    aunts=f.read().splitlines()
    aunts=[item.split(': ',1)[1] for item in aunts]
    aunts=[item.replace(':','').replace(',','') for item in aunts]
    aunts=[item.split(' ') for item in aunts]
    criterions=[]
    for aunt in aunts:
        criterion=[item for item in aunt if not item.isdigit()]
        criterions=list(set(criterions+criterion))

    infos=[[-1 for x in range(len(criterions))] for y in range(len(aunts))]
    for i in range(len(aunts)):
        for c in range(3):
            infos[i][criterions.index(aunts[i][2*c])]=int(aunts[i][2*c+1])

with open("infos_sue.txt") as f:
    temp=f.read().splitlines()
    temp=[item.split(': ') for item in temp]
    infos_sue=[0 for x in range(len(temp))]
    for i in range(len(temp)):
        infos_sue[criterions.index(temp[i][0])]=int(temp[i][1])
    
for sue in range(len(aunts)):
    score=1
    for i in range(len(infos_sue)):
        if infos[sue][i] != -1 :
            if infos[sue][i]!=infos_sue[i]: score=0
    if score==1 : print("PART I :", sue+1)


for sue in range(500):
    score=1
    for i in range(len(infos_sue)):
        if infos[sue][i] != -1 :
            if criterions[i] in ['cats','trees']:
                if infos[sue][i]<=infos_sue[i]: score=0
            elif criterions[i] in ['pomeranians','goldfish']:
                if infos[sue][i]>=infos_sue[i]: score=0
            elif infos[sue][i]!=infos_sue[i]: score=0
    if score==1 : print("PART II :", sue+1)

   # print(aunts)

#    In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).