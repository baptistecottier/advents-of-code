def generator(input) : 
    return input

def part_1(input) :
    for i in range(10, 26):
        print("[[bin]]\nname= \""+str(i)+"\"\npath=\"../../"+str(i)+"/"+str(i)+".rs\"\n\n")
    return solver(input, 4)
    
def part_2(input) :
    return solver(input, 14)
        
def solver(input, size) : 
    for i in range(len(input)-size) : 
        if len(set(input[i:i+size]))==size : 
            return i+size