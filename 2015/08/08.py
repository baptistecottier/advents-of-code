def parser(data): 
    return data.splitlines()

def solver(strings):
    yield sum(len(string) - len(eval(string)) for string in strings)
    yield sum(2 + string.count('\"') + string.count('\\') for string in strings)
