def preprocessing(data): 
    return data.splitlines()


def solver(strings):
    decoded = 0
    encoded = 0
    
    for string in strings:
        encoded += len(string) - len(eval(string))
        decoded += 2 + string.count('\"') + string.count('\\')
        
    yield encoded
    yield decoded
