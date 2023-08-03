from aoctools.functions import extract_chunks


def parser(input_):
    boxes = extract_chunks(input_, 3, neg = False, func = sorted)
    return boxes


def solver(dimensions):
    paper  = 0
    ribbon = 0

    for l, w, h in dimensions:
        preprod = l * w
        presum  = 2 * (l + w)
        paper  += 3 * preprod + presum * h
        ribbon += h * preprod + presum

    yield paper
    yield ribbon