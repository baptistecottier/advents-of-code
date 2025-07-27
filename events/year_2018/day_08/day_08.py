"""
Advent of Code - Year 2018 - Day 8
https://adventofcode.com/2018/day/8
"""


def preprocessing(puzzle_input: str) -> list[int]:
    """Converts space-separated string of numbers into a list of integers."""
    return list(map(int, puzzle_input.split(' ')))


def solver(tree: list[int]) -> tuple[int, int]:
    """
    Solve the tree puzzle by reading tree structure and returning metadata sum and root value.

    Args:
        tree: List of integers representing the tree structure in specific format.

    Returns:
        tuple[int, int]: Metadata sum and root node value.

    Examples:
        >>> solver([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])
        (138, 66)
        >>> solver([0, 1, 99])
        (99, 99)
    """
    tree_infos = read_tree(tree)
    return tree_infos[0], tree_infos[1]


def read_tree(data: list[int]) -> tuple[int, int, list[int]]:
    """Parse a tree structure from a flat list of integers and calculate metadata sums.

    Args:
        data: List of integers representing tree structure [children_count, metadata_count, ...]

    Returns:
        tuple: (total_metadata_sum, node_value, remaining_data)
               - total_metadata_sum: Sum of all metadata in tree
               - node_value: Node's value (metadata sum if leaf, sum of referenced children if not)
               - remaining_data: Unprocessed portion of input data

    Examples:
        >>> read_tree([0, 3, 10, 11, 12])
        (33, 33, [])
        >>> read_tree([1, 1, 0, 1, 99, 2])
        (101, 0, [])
    """
    children, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for _ in range(children):
        total, score, data = read_tree(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0:
        return (totals, sum(data[:metas]), data[metas:])
    return (totals, sum(scores[k - 1] for k in data[:metas] if k <= len(scores)), data[metas:])
