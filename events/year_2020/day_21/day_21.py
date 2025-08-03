"""
Advent of Code - Year 2020 - Day 21
https://adventofcode.com/2020/day/21
"""

from parse import parse, Result


def preprocessing(puzzle_input) -> tuple[dict[str, set[str]], dict[str, int]]:
    """
    Parses input to map allergens to possible ingredients and count ingredient occurrences.
    """
    detector = {}
    list_ingredients = {}

    for food in puzzle_input.splitlines():
        result = parse("{} (contains {})", food)
        if not isinstance(result, Result):
            raise ValueError("Incorrect input format!")
        ingredients, allergens = result
        ingredients = ingredients.split(' ')
        allergens = allergens.split(', ')

        for allergen in allergens:
            if allergen in detector:
                detector[allergen] = {ing for ing in ingredients if ing in detector[allergen]}
            else:
                detector[allergen] = set(ingredients)

        for ingredient in ingredients:
            if ingredient in list_ingredients:
                list_ingredients[ingredient] += 1
            else:
                list_ingredients[ingredient] = 1

    return detector, list_ingredients


def solver(detector: dict[str, set[str]], list_ingredients: dict[str, int]) -> tuple[int, str]:
    """
    Solves for the number of safe ingredients and returns a canonical dangerous ingredient list
    based on allergen detection and ingredient occurrences.
    """
    safe = set()
    for ingredient in list_ingredients:
        if all(ingredient not in allergens for allergens in detector.values()):
            safe.add(ingredient)

    while any(len(allergens) != 1 for allergens in detector.values()):
        for allergens in detector.values():
            if len(allergens) == 1:
                a = list(allergens)[0]
                for key, value in detector.items():
                    if allergens < value:
                        detector[key].remove(a)

    return (sum(list_ingredients[ingredient] for ingredient in safe),
            ','.join(detector[ingredient].pop() for ingredient in sorted(detector)))
