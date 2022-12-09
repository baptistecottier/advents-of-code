def generator(input) : 
    return input.splitlines()

def part_1(input) :
    return sum([item for item in solver(input) if item <= 100_000])
        
def part_2(input) :
    total_size = max(solver(input))
    return min([item for item in solver(input) if item > (total_size - 40_000_000)])
       
        
def solver(input) :
    sizes = {}
    path =["root"]
    for command in input:
        details = command.split(' ')
        match details: 
            case ["$","cd","/"] : path = ["root"]
            case ["$","cd",".."] : path.pop()
            case ["$","cd",_] : path.append("".join(path)+details[2])
            case ["dir",_] : pass 
            case ["$","ls"] : pass 
            case _ : 
                for folder in path : 
                    if folder in sizes : sizes[folder]+=int(details[0])
                    else : sizes[folder] = int(details[0])
    return [sizes[item] for item in sizes]