from pythonfw.functions import screen_reader


def preprocessing(input): 
    dots, folds = input.split('\n\n')
    dots  = {eval(dot) for dot in dots.splitlines()}
    folds = [(fold[11], int(fold[13:])) for fold in folds.splitlines()]
    return dots, folds
    
    
def solver(dots, folds):
    
    for k, (axis, n) in enumerate(folds):
        if axis == 'x': dots = {(min(x, 2 * n - x), y) for (x, y) in dots}
        if axis == 'y': dots = {(x, min(y, 2 * n - y)) for (x, y) in dots}
        if k == 0: yield len(dots)

    yield screen_reader(dots)
