def generator(input) :
    return [int(item) for item in input.splitlines()]


def part_1(input) : 
    return solver(input, 1)


def part_2(input) : 
    return solver([811589153 * i for i in input], 10)
    
    
def solver(cipher_list, rep) :
    l = len(cipher_list)
    index_list = [i for i in range(l)]
    
    for _ in range(rep):
        for i in range(l):
            c = cipher_list[i]
            prev_ind = index_list.index(i)
            index_list.remove(i)
            index_list.insert((c + prev_ind) % (l-1) , i)
        
    z = index_list.index(cipher_list.index(0))
    v = sum([cipher_list[index_list[(z + i) % l]] for i in [1000, 2000, 3000]])
    return v