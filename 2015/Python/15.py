import numpy

with open("Day15/input.txt") as f:
    ingredients=f.read().splitlines()
    values=[]
    infos=[]
    for ingredient in ingredients:
        values=ingredient.split(': ')[1].replace(',','')
        values=[int(values.split(' ')[i]) for i in range(1,10,2)]
        infos.append(values)
    
    max_score=0
    score=[0 for i in range(5)]
    for f in range(100):
        for c in range(1,100-f):
            for b in range(1,100-c-f):
                s=100-f-c-b
                for i in range(5):
                    score[i]=max(f*infos[0][i]+c*infos[1][i]+b*infos[2][i]+s*infos[3][i],0)
                if score[4]==500 : max_score=max(numpy.prod(score[:-1]), max_score)
              
    print(max_score)