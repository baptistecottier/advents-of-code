table=[[1000 for x in range(8)] for y in range(8
)]
with open("Day9/input.txt") as f:
    distances=f.read().splitlines()
    cities=list(set([distance.split(' to ')[0] for distance in distances]))+['Arbre']

    for distance in distances:
        towns,kms = distance.split(' = ')
        town_A, town_B = towns.split(' to ')
        table[cities.index(town_A)][cities.index(town_B)]=int(kms)
        table[cities.index(town_B)][cities.index(town_A)]=int(kms)
    print(table, cities)

    clc=[1000 for x in range(7)]
    import numpy as np 
    shortest_distance=0
    for a in range(8):
        print(a)
        liste1=list(set(list(range(8))) - set([a]))
        print(liste1)
        for b in liste1:
            clc[0]=table[a][b]
            liste2=list(set(liste1) - set([b]))
            for c in liste2:
                clc[1]=table[b][c]
                liste3=list(set(liste2) - set([c]))
                for d in liste3:
                    clc[2]=table[c][d]
                    liste4=list(set(liste3) - set([d]))
                    for e in liste4:
                        clc[3]=table[d][e]
                        liste5=list(set(liste4) - set([e]))
                        for f in liste5:
                            clc[4]=table[e][f]
                            liste6=list(set(liste5) - set([f]))
                            for g in liste6:
                                clc[5]=table[f][g]
                                liste7=list(set(liste6) - set([g]))
                                for h in liste7:
                                    clc[6]=table[g][h]
                                    if shortest_distance < sum(clc):
                                        print(clc, sum(clc))
                                        shortest_distance=sum(clc)
                                        shortest_clc = clc 
print(shortest_distance, sum(shortest_clc))