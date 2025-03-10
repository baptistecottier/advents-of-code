"""Advent of Code - Year 2015 - Day 15"""

from collections           import defaultdict
from math                  import prod
from pythonfw.functions    import extract_chunks


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """Extract ingredient properties from puzzle input into chunks of 5 values.
    
    Args:
        puzzle_input: Raw puzzle input string
    Returns:
        List of lists, each containing 5 numeric values per ingredient
    """
    return extract_chunks(puzzle_input, 5)


def solver(ingredients: list[list[int]]):
    """
    Calculate the highest possible cookie score based on ingredient combinations.

    This function evaluates different combinations of ingredients to find the optimal cookie recipe
    that yields the highest score, both overall and for a specific calorie count (500).

    Args:
        ingredients (list[list[int]]): A list of lists where each inner list contains 5 integers
            representing the properties of an ingredient in the following order:
                [capacity, durability, flavor, texture, calories]

    Returns:
        tuple[int, int]: A tuple containing:
            - First element: The highest possible score for any combination of ingredients
            - Second element: The highest possible score for combinations that total exactly 500
              calories

    Notes:
        - Each ingredient property is multiplied by the number of teaspoons used (0-100)
        - Total teaspoons used must equal 100
        - Final score is the product of all properties (excluding calories)
        - Negative property values in the final calculation are treated as 0
    """
    nb_ing = len(ingredients)
    frosting, candy, butterscotch, sugar = ingredients + (4 - nb_ing) * [[0, 0, 0, 0, 0]]

    frosting     = {i: [i * item for item in frosting]     for i in range(101)}
    candy        = {i: [i * item for item in candy]        for i in range(101)}
    butterscotch = {i: [i * item for item in butterscotch] for i in range(101)}
    sugar        = {i: [i * item for item in sugar]        for i in range(101)}
    scores       = defaultdict(list)

    for i in range(101):
        f = frosting[i]
        for j in range(101 - i):
            b = candy[j]
            for k in range(101 - (i + j)):
                c     = butterscotch[k]
                s     = sugar[100 - (i + j + k)]
                score = prod(max(0, sum(v[index] for v in [f, b, c, s])) for index in range(4))
                scores[sum(v[4] for v in [f, b, c, s])].append(score)

    return (max(sum(scores.values(), [])), max([0, *scores[500]]))
