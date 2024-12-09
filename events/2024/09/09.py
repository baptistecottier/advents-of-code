def preprocessing(input):
    return input

def solver(disk):
    disk = [int(item) for item in disk]
    memory = []
    id = 0
    for n in range(0, len(disk), 2):
        memory += [id] * disk[n]
        try: 
            memory += [-1] * disk[n+1]
        except: 
            pass
        id += 1

    checksum = 0
    r = 0
    while memory:
        a = memory.pop(0)
        try: 
            while a == -1:
                a = memory.pop()
            checksum += r * a
            r += 1
        except: 
            break
            
        
    yield checksum
    
    memory = []
    id = 0
    for n in range(0, len(disk), 2):
        memory += [(id, disk[n])]
        try: 
            memory += [(-1 , disk[n+1])]
        except: 
            pass
        id += 1

    for i in range(len(memory) - 1, -1, -1):
        (a, n) = memory[i]

        if a == -1:
            continue
        for j, (b, m) in enumerate(memory):
            if (b == -1):
                if (n < m):
                    memory = memory[:j] + [(a, n), (-1, m - n)] + memory[j + 1:]
                    i -= 1
                    break
                if n == m:
                    memory = memory[:j] + [(a, n)] + memory[j + 1:]
                    break
            
    new_memory = []
    v = set()
    while memory:
        (a, n) = memory.pop(0)
        if a in v:
            new_memory += [0] *n
        else:
            v.add(a)
            new_memory += [a] * n

    checksum = 0
    for i, n in enumerate(new_memory):
        checksum += i * max(0,n)      

    yield checksum
        