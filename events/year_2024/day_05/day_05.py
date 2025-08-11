"""
Advent of Code - Year 2024 - Day 5
https://adventofcode.com/2024/day/5
"""


def preprocessing(puzzle_input: str) -> tuple[list[int], list[tuple[int, list[int]]]]:
    """
    Puzzle input contains two parts. The first one contains ordering rules and the second one a
    list of updates. We associate each update with an initial value of 0 supposing the update does
    not need to be ordered, for further purpose.
    """
    raw_rules, raw_updates = puzzle_input.split('\n\n')
    rules, updates = [], []

    for rule in raw_rules.splitlines():
        rules.append([int(page) for page in rule.split('|')])

    for update in raw_updates.splitlines():
        updates.append((0, [int(page) for page in update.split(',')]))
    return rules, updates


def solver(rules: list[int], updates: list[tuple[int, list[int]]]) -> list[int]:
    """
    Processes a list of updates according to given rules and returns the sum of middle page values
    for each order type.
    """
    middle_page_sum = [0, 0]

    while updates:
        to_order, update = updates.pop()
        ordered = True
        for i in range(len(update) - 1):
            if [update[i], update[i + 1]] not in rules:
                update[i], update[i + 1] = update[i + 1], update[i]
                updates.append((1, update))
                ordered = False
                break
        if ordered:
            middle_page_sum[to_order] += update[len(update) // 2]

    return middle_page_sum
