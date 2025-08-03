"""
Advent of Code - Year 2020 - Day 7
https://adventofcode.com/2020/day/7
"""


def preprocessing(puzzle_input: str) -> dict[str, list[tuple[int, str]]]:
    """
    Parses the puzzle input describing bag containment rules into a dictionary mapping each bag
    color to a list of (count, contained bag color) tuples.
    """
    all_bags = {}
    puzzle_input = puzzle_input.replace("bags", "").replace("bag", "").replace(".", "")

    for rule in puzzle_input.splitlines():
        color, bags = rule.split("  contain ")[:2]
        if 'no other' in rule:
            bags = []
        else:
            bags = [b.strip().split(" ", 1) for b in bags.split(",")]
            bags = [[int(n), b] for n, b in bags]
        all_bags[color] = bags

    return all_bags


def solver(rules: dict[str, list[tuple[int, str]]]) -> tuple[int, int]:
    """
    Counts how many bag colors can eventually contain a "shiny gold" bag and the total number of
    bags required inside a "shiny gold" bag.
    """
    candidates = ["shiny gold"]
    answer = set()

    while candidates:
        candidate = candidates.pop()
        for color in rules.keys():
            if candidate in (c for _, c in rules[color]):
                candidates.append(color)
                answer.add(color)

    return len(answer), count_bags("shiny gold", rules) - 1


def count_bags(color: str, rules):
    """
    Recursively counts the total number of bags contained within a bag of the given color,
    including itself, based on the provided containment rules.
    """
    return 1 + sum(n * count_bags(c, rules) for n, c in rules[color])
