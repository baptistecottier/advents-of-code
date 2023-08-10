def preprocessing(input): 
    return input
            
def solver(buffer): 
    size = 4
    for i, _ in enumerate(buffer): 
        if len(set(buffer[i:i + size])) == size: 
            yield i + size
            if size == 14: break 
            else: size += 10