from json import loads
import builtins

def parser(input): 
    return loads(input)

def solver(document):
    yield get_sum(document, True)
    yield get_sum(document, False)

def get_sum(document ,allow_red):
    match (type(document), allow_red):
        case builtins.int, _:  return document
        case builtins.list, _: return sum(get_sum(subdocument , allow_red) for subdocument in document)
        case builtins.dict, True: return get_sum(list(document.values()), allow_red)
        case builtins.dict, False: return ('red' not in document.values()) * get_sum(list(document.values()), allow_red)
        case _: return 0
        