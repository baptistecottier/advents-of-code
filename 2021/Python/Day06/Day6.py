map=[0 for x in range(9)]

with open("Day6/input.txt") as f: 
    fishes=[int(item) for item in f.read().split(',')]
    for fish in fishes:
        map[fish]+=1

for day in range(256):
    temp=map[0]
    map=[map[(i+1)] for i in range(8)]
    map.append(temp)
    map[6]+=temp
print(sum(map))    
