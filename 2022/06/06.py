def solver(buffer): 
    size = 4
    for i in range(len(buffer)): 
        if len(set(buffer[i:i + size])) == size: 
            yield i + size
            if size == 14: break 
            else: size += 10