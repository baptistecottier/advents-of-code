from parse       import parse
from collections import defaultdict


def preprocessing(input_):
    tree = {}
    for node in input_.splitlines():
        name, weight, children = parse("{} ({:d}{}", node)
        children = children[5:].split(', ')
        tree[name] = {"weight": weight, "children": children if children != [''] else []}
    return tree


def solver(tree): 
    list_children = sum((node["children"] for node in tree.values()), [])
    for name in tree.keys():
        if name not in list_children:
            root = name
            yield root
            break
    
    for name, infos in tree.items():
        tree[name]["sum_weight"] = sum_weight(tree, name)
        
    for name, infos in sorted(tree.items(), key = lambda x : x[1]["sum_weight"]):
        if infos["children"]:
            weights = defaultdict(list)
            for child in infos["children"]: weights[tree[child]["sum_weight"]].append(child) 
            if len(weights) != 1:
                weights = sorted(weights.items(), key = lambda x : len(x[1]))
                (u_weight, u_name), (b_weight, _) = weights
                yield tree[u_name.pop()]["weight"] + b_weight - u_weight
                return


def sum_weight(tree, child):
    if tree[child]["children"] == ['']: 
        return tree[child]["weight"]
    else:
        return tree[child]["weight"] + sum(sum_weight(tree, c) for c in tree[child]["children"])