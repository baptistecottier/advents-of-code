with open("Day12/input") as f:
    channels=f.read().replace('\n','-').split('-')
    caves=list(set(channels))
    print(caves)
    paths=[[0 for x in range(len(caves))] for y in range(len(caves))]
    for i in range(0,len(channels), 2):
        paths[caves.index(channels[i])][caves.index(channels[i+1])]=1
        paths[caves.index(channels[i+1])][caves.index(channels[i])]=1
    print(paths)

    good_paths=0


    def count_paths(caves, matrix_z, sp_x , path_list, UC, cnt):
        matrixes=[]
        matrix=matrix_z.copy()
        if sp_x==caves.index('end') : 
            if path_list.count('start')>1: return 0
            else : return 1
        elif sum(matrix[sp_x])==0 or (cnt==1 and caves[sp_x] in UC) : return 0
        else : 
            outs=[n for n in range(len(matrix[sp_x])) if matrix[sp_x][n]==1]
            if ord(caves[sp_x][0]) >= 97 : 
                if caves[sp_x] in UC : cnt=1
                else : UC.append(caves[sp_x])
            return sum([count_paths(caves, matrix, i, path_list+[caves[i]], UC.copy(), cnt) for i in outs])

        
    print(count_paths(caves, paths, caves.index('start'), ['start'], [], 0))


    # import numpy as np
    # adj=np.array(paths)
    # enter='start'
    # m=adj
    # score=0

    # print(score)













    # for x in range(3):
    #     m=np.dot(m,adj)
    #     score+=m[caves.index('start')][caves.index('end')]