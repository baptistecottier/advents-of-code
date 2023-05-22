import math, re


def generator(input): 
    ingredients = tuple(int(n) for n in re.findall(r'[-]?[0-9]+', input))
    return tuple(ingredients[i: i + 5] for i in range(0, 20, 5))

def part_1(ingredients): 
    return find_best_cookie_score(ingredients)

def part_2(ingredients):
    return find_best_cookie_score(ingredients, True)


def find_best_cookie_score(ingredients, fixed_calories = False):
    best_score = 0
    frosting, candy, butterscotch, sugar = ingredients
    frosting = {i: [i * item for item in frosting] for i in range(101)}
    candy = {i: [i * item for item in candy] for i in range(101)}
    butterscotch = {i: [i * item for item in butterscotch] for i in range(101)}
    sugar = {i: [i * item for item in sugar] for i in range(101)}
    for i in range(100):
        f = frosting[i]
        for j in range(100 - i):
            b = butterscotch[j]
            for k in range(100 - (i + j)):
                c = candy[k]
                s = sugar[100 - (i + j + k)]
                score = math.prod(max(0, sum([v[index] for v in [f, b, c, s]])) for index in range(4))
                if  score > best_score:
                    if not fixed_calories or sum(v[4] for v in [f, b, c, s]) == 500:
                        best_score = score
    return best_score