from hashlib import md5

def generator(input): return input

def part_1(input): return solver([],input, 0, 0, len(input))[0]

def part_2(input):  return len(solver([],input, 0, 0, len(input))[-1])


def solver(paths,path,x,y,l):
    d={'U' : (0,1) , 'D' : (0,-1) , 'L' : (-1,0) , 'R': (1,0)}
    if (x,y)==(3,-3) : paths.append(path[l:]) # If the vault is reached, append the path
    else :
        for n in get_neighbours(path): # 
            (tx, ty) = d[n]
            if  0 <= x+tx <= 3 and -3 <= y+ty <= 0 : solver(paths, path+n,x+tx, y+ty,l)
    return sorted(paths , key = len)

def get_neighbours(s): # Fonction to determine the available neighbours
    hash=md5(s.encode()).hexdigest()[:4]
    N=['U', 'D', 'L', 'R']
    nb=[N[i] for i in range(4) if 'b' <= hash[i] <= 'f']
    return nb