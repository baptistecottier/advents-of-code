from json import loads
import builtins


def parser(input): 
    return loads(input)


def solver(document):
    yield get_sum(document, True)
    yield get_sum(document, False)


def get_sum(document, allow_red):
    match type(document):
        case builtins.int:  return document
        case builtins.list: return sum(get_sum(subdocument , allow_red) for subdocument in document)
        case builtins.dict: 
            if allow_red or 'red' not in document.values():
                return get_sum(list(document.values()), allow_red) 
            else:
                return 0
        case _: return 0
        