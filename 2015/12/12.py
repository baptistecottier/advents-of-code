from json import loads
import builtins

def generator(input): 
    return loads(input)

def part_1(document):
    return get_sum(document, True)

def part_2(document): 
    return get_sum(document, False)

def get_sum(item ,allow_red):
    match (type(item), allow_red):
        case builtins.int, _:  return item
        case builtins.list, _: return sum(get_sum(subitem , allow_red) for subitem in item)
        case builtins.dict, True: return get_sum(list(item.values()), allow_red)
        case builtins.dict, False: return ('red' not in item.values()) * get_sum(list(item.values()), allow_red)
        case _: return 0
        