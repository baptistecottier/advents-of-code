from pythonfw.functions import extract_chunks
from dataclasses import dataclass

@dataclass
class Box:
    l: int
    w: int
    h: int


def preprocessing(puzzle_input):
    boxes = list()
    for l, w, h in extract_chunks(puzzle_input, 3, neg = False, func = sorted):
        boxes.append(Box(l, w, h))
    return boxes


def solver(boxes):
    paper  = 0
    ribbon = 0

    for b in boxes:
        preprod = b.l * b.w
        presum  = 2 * (b.l + b.w)
        paper  += 3 * preprod + presum * b.h
        ribbon += b.h * preprod + presum

    yield paper
    yield ribbon