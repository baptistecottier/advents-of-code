def preprocessing(puzzle_input):
    calories = {(int(calories) for calories in reeinder.splitlines()) for reeinder in puzzle_input.split("\n\n")}
    return calories


def solver(calories): 
    calories = sorted(sum(reeinder) for reeinder in calories)
    yield calories[-1]
    yield sum(calories[-3:])
