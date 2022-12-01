from hashlib import md5

def get_neighbours(s): # Fonction to determine the available neighbours
    hash=md5(s.encode()).hexdigest()[:4]
    N=['U', 'D', 'L', 'R']
    nb=[N[i] for i in range(4) if 'b' <= hash[i] <= 'f']
    return nb


def get_paths(paths,path,x,y):
    if (x,y)==(3,-3) : paths.append(path[len(input):]) # If the vault is reached, append the path
    else :
        for n in get_neighbours(path): # 
            (tx, ty) = d[n]
            # If we are still on the grid and not witht the vault, continue computing paths
            if  0 <= x+tx <= 3 and -3 <= y+ty <= 0 : get_paths(paths, path+n,x+tx, y+ty)
    return sorted(paths , key = len)

d={'U' : (0,1) , 'D' : (0,-1) , 'L' : (-1,0) , 'R': (1,0)}


input='pvhmgsws'
paths=get_paths([],input, 0, 0)

print('Let\'s go to the secure vault ! The shortest path to access it is', paths[0])
print('and is', len(paths[0]), 'steps long, while the longest path is', len(paths[-1]), 'steps long.')
