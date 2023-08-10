def preprocessing(input):
    return {(int(calories) for calories in reeinder.splitlines()) for reeinder in input.split("\n\n")}

def solver(input): 
    calories = sorted(sum(reeinder) for reeinder in input)
    yield calories[-1]
    yield sum(calories[-3:])
