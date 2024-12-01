from itertools import product

def preprocessing(data: str): 
    return list(map(int, data.split()))

def solver(lengths):
    if len(lengths) % 3 == 0:
        yield count_possible_triangles(lengths[i: i + 3] for i in range(0, len(lengths), 3))
    if len(lengths) % 9 == 0: 
        vertical = ((lengths[i + j],     \
                 lengths[i + j + 3], \
                 lengths[i + j + 6]) for i, j in product(range(0, len(lengths), 9), range(3)))
        yield count_possible_triangles(vertical)


def count_possible_triangles(triangles):
    return sum(sum(triangle) > 2 * max(triangle) for triangle in triangles)
