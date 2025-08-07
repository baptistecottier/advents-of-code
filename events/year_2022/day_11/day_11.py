"""
Advent of Code - Year 2022 - Day 11
https://adventofcode.com/2022/day/11
"""

from collections.abc import Callable, Iterator
from math import prod


def preprocessing(puzzle_input: str
                  ) -> tuple[list[tuple[int, int]], list[Callable], list[tuple[int, ...]]]:
    """
    Parses the puzzle input into starting items, operation functions, and predicates for each
    monkey.
    """
    monkeys = puzzle_input.split('\n\n')
    starting_items = []
    funcs = []
    pred = []

    for i, monkey in enumerate(monkeys):
        details = monkey.splitlines()[1:]
        items = details[0].split(': ')[1]
        starting_items += [(int(item), i) for item in items.split(', ')]

        match (details[1].split('= old ')[1]).split(' '):
            case ('*', 'old'): funcs.append(lambda x: x ** 2)
            case ('*', n): funcs.append(lambda x, n=int(n): x * n)
            case (_, n): funcs.append(lambda x, n=int(n): x + n)

        pred.append(tuple(int(line.split(' ')[-1]) for line in details[2:]))

    return starting_items, funcs, pred


def solver(items: list[tuple[int, int]], funcs: list[Callable], tests: list[tuple[int, ...]]
           ) -> Iterator[int]:
    """
    Yields the result of monkey_business for two sets of parameters, iterating over specified
    rounds and worry level divisors.
    """
    for rounds, worry_level_div in ((20, 3), (10_000, 1)):
        yield monkey_business(items, funcs, tests, rounds, worry_level_div)


def monkey_business(
        items: list[tuple[int, int]],
        funcs: list[Callable],
        tests: list[tuple[int, ...]],
        rounds: int,
        worry_level_div: int) -> int:
    """
    Simulates a monkey business process over a number of rounds, applying functions and tests to
    items, and returns the product of the two highest inspection counts.
    """
    modulo = prod([mod for mod, _, _ in tests])
    inspected_items = [0 for _ in funcs]

    for old, new_monkey in items:
        for _ in range(rounds):
            old_monkey = 0
            while new_monkey >= old_monkey:
                func = funcs[new_monkey]
                pred = tests[new_monkey]
                inspected_items[new_monkey] += 1
                old = (func(old) // worry_level_div) % (worry_level_div * modulo)
                old_monkey, new_monkey = new_monkey, pred[1 + (old % pred[0] != 0)]

    return prod(sorted(inspected_items)[-2:])
