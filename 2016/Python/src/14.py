with open("Day14/input.txt") as f:
    renes=f.read().splitlines()
    infos=[]
    for rene in renes:
        words=rene.replace('.','').split(' ')
        infos+=[[words[0], int(words[3]) , int(words[6]) , int(words[-2])]]
    
    t=2503
    score=[0 for i in range(len(renes))]
    points=[0 for i in range(len(renes))]
    for time in range(1,t+1):
        max_distance=0
        for i in range(len(infos)):
            info=infos[i]
            distance=(time//(info[2]+info[3]))*info[1]*info[2]
            if time % (info[2]+info[3]) > info[2] :
                distance += info[2] * info[1]
            else : 
                distance += info[1] * (time % (info[2]+info[3]))
            max_distance=max(distance, max_distance)
            score[i]=distance
        for i in range(len(renes)):
            if score[i]==max_distance : points[i]+=1
    print(points)




# Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
