from pythonfw.functions import extract_chunks
from dataclasses import dataclass

# On définit une classe pour les box
@dataclass
class Box:
    l: int
    w: int
    h: int

# On parse l'input de sorte à récupérer les dimensions des boîtes. 
# On les trie ensuite pour pouvoir déterminer la surface minimale.
def preprocessing(puzzle_input):
    boxes = list()
    for l, w, h in extract_chunks(puzzle_input, 3, neg = False, func = sorted):
        boxes.append(Box(l, w, h))
    return boxes

# Une fois la deuxième partie découverte, on peut noter que des
# calculs intermédiaires sont communs aux deux parties (preprod et presum)
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