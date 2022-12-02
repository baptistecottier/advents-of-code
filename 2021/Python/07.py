from statistics import mean, median

with open("Day7/input.txt") as f:
    dist=0
    positions=[int(item) for item in f.read().split(',')]
    med=int(median(positions))
    for crab in positions:
        dist+=abs(crab-med)
    print("Part I : ", dist)

    dist=0
    mean=int(mean(positions))
    for crab in positions:
        n=abs(crab-mean)
        dist+=n*(n+1)/2
    print("Part II : ", int(dist))
   