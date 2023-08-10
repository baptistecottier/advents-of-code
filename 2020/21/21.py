from parse import parse

def preprocessing(input_):
    detector = {}
    list_ingredients = {}
    
    for food in input_.splitlines():
        ingredients, allergens = list(parse("{} (contains {})", food))
        ingredients = ingredients.split(' ')
        allergens = allergens.split(', ')
        for allergen in allergens: 
            if allergen in detector :
                detector[allergen] = {ingredient for ingredient in ingredients if ingredient in detector[allergen]}
            else: 
                detector[allergen] = set(ingredients)
        for ingredient in ingredients: 
            if ingredient in list_ingredients:
                list_ingredients[ingredient] += 1
            else: 
                list_ingredients[ingredient] = 1
    return detector, list_ingredients

def solver(input_):
    yield part_1(input_)
    yield part_2(input_)
        
def part_1(input_): 
    detector, list_ingredients = input_
    safe = {ingredient for ingredient in list_ingredients if (all(ingredient not in allergen for allergen in detector.values()))}
    return sum(list_ingredients[ingredient] for ingredient in safe)

def part_2(input_): 
    detector, _ = input_
    while any(len(allergen) != 1 for allergen in detector.values()):
        for allergen in detector.values():
            if len(allergen) == 1:
                a = next(iter(allergen))
                for key, value in list(detector.items()):
                    if allergen < value: 
                        detector[key].remove(a)
    return ','.join(detector[ingredient].pop() for ingredient in sorted(list(detector.keys())))