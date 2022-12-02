with open("Day14/input") as f:
    input=f.read().splitlines()
    transformations=input[2:]
    molecule=input[0]


atom_start=[transformation.split(' -> ')[0] for transformation in transformations]
atom_end=[transformation.split(' -> ')[1] for transformation in transformations]
counter_couple=[[atom_start[i], molecule.count(atom_start[i]),atom_end[i]] for i in range(len(atom_start))]

for steps in [10, 40]:
    new_count=[counter_couple[i][1] for i in range(len(counter_couple))]
    for count in range(steps):
        for item in [item.copy() for item in counter_couple if item[1] != 0]:
            pair1=item[0][0]+item[2]
            pair2=item[2]+item[0][1]
            new_count[atom_start.index(pair1)]+=item[1]
            new_count[atom_start.index(pair2)]+=item[1]
            new_count[atom_start.index(item[0])]-=item[1]
        for i in range(len(counter_couple)): counter_couple[i][1]=new_count[i]


    letters=list(set(atom_end))
    letter_count=[0 for i in letters]

    # On ajoute un pour les lettres aux extrémités qui ne seront comptés qu'une seule fois
    for n in [0,-1] : letter_count[letters.index(molecule[n])]=1 
    for duo , value, _ in counter_couple :
        for ch in duo:
            letter_count[letters.index(ch)]+=value

    print("Part", 1+(steps==40) , ": " , int((max(letter_count)-min(letter_count))/2))

