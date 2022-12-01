from random import shuffle


def nth_repl(s, sub, repl, n):
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        return s[:find] + repl + s[find+len(sub):]
    return s

with open("Day19/input") as f:
    input=f.read().splitlines()
    transformations=input[:-2]
    mol=input[-1]
transformations=[transformation.split(' => ') for transformation in transformations]
transformations.sort(key=lambda item : len(item[1]))

created_mols=[]
for atom_a, atom_z in transformations:
    for i in range(mol.count(atom_a)):
        created_mols+=[nth_repl(mol,atom_a,atom_z,i+1)]

count=len(list(set(created_mols)))
print(count)

target = mol
part2 = 0

while target != 'e':
    tmp = target
    for a, b in transformations:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    if tmp == target:
        target = mol
        part2 = 0
        shuffle(transformations)

print(part2)