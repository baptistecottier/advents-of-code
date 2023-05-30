from itertools import product

def generator(input: str): 
    return list(int(item) for item in input.split())

def part_1(lengths):
    triangles = list(lengths[i: i + 3] for i in range(0, len(lengths), 3))
    return count_possible_triangles(triangles)

def part_2(lengths):
    triangles = list((lengths[i + j],     \
                      lengths[i + j + 3], \
                      lengths[i + j + 6]) for i, j in product(range(0, len(lengths), 9), range(3)))
    return count_possible_triangles(triangles)


def count_possible_triangles(triangles):
    return sum(sum(triangle) > 2 * max(triangle) for triangle in triangles)
