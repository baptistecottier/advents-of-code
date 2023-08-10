def preprocessing(input):
    return [int(item) for item in input.splitlines()]

def solver(file):
    yield mix(file, 1)
    yield mix([811589153 * i for i in file], 10)
    
    
def mix(cipher_list, rep):
    nb_cipher = len(cipher_list)
    index_list = list(range(nb_cipher))
    
    for _ in range(rep):
        for index, cipher in enumerate(cipher_list):
            prev_index = index_list.index(index)
            index_list.remove(index)
            index_list.insert((cipher + prev_index) % (nb_cipher - 1) , index)
        
    zero_index = index_list.index(cipher_list.index(0))
    return sum([cipher_list[index_list[(zero_index + shift) % nb_cipher]] for shift in [1000, 2000, 3000]])