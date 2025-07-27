"""
Advent of Code - Year 2017 - Day 7
https://adventofcode.com/2017/day/7
"""

from collections import defaultdict
from parse import parse, Result


def preprocessing(puzzle_input: str) -> dict[str, dict]:
    """
    Parse puzzle input as a dict, refering weight and children nodes

    Example
        >>> preprocessing("ktlj (57)\nfwft (72) -> ktlj")
        {'ktlj': {'weight': 55, 'children': []},  }
    """
    tree = {}
    for node in puzzle_input.splitlines():
        result = parse("{} ({:d}{}", node)
        if isinstance(result, Result):
            name, weight, children = result
            children = children[5:].split(", ")
            tree[name] = {
                "weight": weight,
                "children": children if children != [""] else [],
            }
    return tree


def solver(tree: dict[str, dict]) -> tuple[str, int]:
    """
    Solve a tree balancing problem.

    Find the root node and the unbalanced node's corrected weight.

    Args:
        tree: Dictionary where keys are node names and values are node info dicts with
             'weight', 'children', and optionally 'sum_weight' keys.
    """
    root = ""
    list_children = sum((node["children"] for node in tree.values()), [])
    for name in tree.keys():
        if name not in list_children:
            root = name
            break

    for name, infos in tree.items():
        tree[name]["sum_weight"] = sum_weight(tree, name)

    for name, infos in sorted(tree.items(), key=lambda x: x[1]["sum_weight"]):
        if infos["children"]:
            weights = defaultdict(list)
            for child in infos["children"]:
                weights[tree[child]["sum_weight"]].append(child)
            if len(weights) != 1:
                weights = sorted(weights.items(), key=lambda x: len(x[1]))
                (u_weight, u_name), (b_weight, _) = weights
                return root, tree[u_name.pop()]["weight"] + b_weight - u_weight

    raise ValueError("Impossible to balance the node's weight")


def sum_weight(tree: dict[str, dict], child: str) -> int:
    """
    Calculate the total weight of a node and all its children in a tree structure.

    Args:
        tree (dict[str, dict]): A dictionary representing the tree where each node contains
            a 'weight' value and list of 'children'.
        child (str): The key/name of the current node to calculate weight for.

    Returns:
        int: The sum of the current node's weight plus all its children's weights recursively.

    Example:
        >>> tree = {
        ...     'a': {'weight': 5, 'children': ['b', 'c']},
        ...     'b': {'weight': 3, 'children': []},
        ...     'c': {'weight': 2, 'children': []}
        ... }
        >>> sum_weight(tree, 'a')
        10
    """
    weight = tree[child]["weight"]
    if tree[child]["children"] != []:
        weight += sum(sum_weight(tree, c) for c in tree[child]["children"])
    return weight
