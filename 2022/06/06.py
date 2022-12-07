def generator(input) : 
    return input
    
def part_2(input) :
    return solver(input, 14)
        
def solver(input, size) : 
    for i in range(len(input)-size) : 
        if len(set(input[i:i+size]))==size : 
            return i+size
