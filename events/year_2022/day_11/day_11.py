"""
Advent of Code - Year 2022 - Day 11
https://adventofcode.com/2022/day/11
"""

from collections.abc import Callable, Iterator
from math import prod


# Simple picklable functions instead of lambdas
def square(x):
    """Square operation: x ** 2."""
    return x ** 2


def preprocessing(puzzle_input: str
                  ) -> tuple[list[tuple[int, int]], list[tuple[str, int]], list[tuple[int, ...]]]:
    """
    Parses the puzzle input into starting items, operation descriptions, and predicates.
    Instead of storing lambda functions (which can't be pickled), we store operation descriptions.
    """
    monkeys = puzzle_input.split('\n\n')
    starting_items = []
    operations = []  # Store ('op_type', value) instead of functions
    pred = []

    for i, monkey in enumerate(monkeys):
        details = monkey.splitlines()[1:]
        items = details[0].split(': ')[1]
        starting_items += [(int(item), i) for item in items.split(', ')]

        match (details[1].split('= old ')[1]).split(' '):
            case ('*', 'old'):
                operations.append(('square', 0))
            case ('*', n):
                operations.append(('multiply', int(n)))
            case (_, n):
                operations.append(('add', int(n)))

        pred.append(tuple(int(line.split(' ')[-1]) for line in details[2:]))

    return starting_items, operations, pred


def apply_operation(op_type: str, value: int, worry_level: int) -> int:
    """Apply the operation to worry level based on operation type."""
    if op_type == 'square':
        return worry_level ** 2
    if op_type == 'multiply':
        return worry_level * value
    if op_type == 'add':
        return worry_level + value
    raise ValueError(f"Unknown operation: {op_type}")


def solver(items: list[tuple[int, int]],
           operations: list[tuple[str, int]],
           tests: list[tuple[int, ...]]) -> Iterator[int]:
    """
    Yields the result of monkey_business for two sets of parameters, iterating over specified
    rounds and worry level divisors.
    """
    for rounds, worry_level_div in ((20, 3), (10_000, 1)):
        yield monkey_business(items, operations, tests, rounds, worry_level_div)


def monkey_business(
        items: list[tuple[int, int]],
        operations: list[tuple[str, int]],
        tests: list[tuple[int, ...]],
        rounds: int,
        worry_level_div: int) -> int:
    """
    Simulates a monkey business process over a number of rounds, applying functions and tests to
    items, and returns the product of the two highest inspection counts.
    """
    modulo = prod([mod for mod, _, _ in tests])
    inspected_items = [0 for _ in operations]

    for old, new_monkey in items:
        for _ in range(rounds):
            old_monkey = 0
            while new_monkey >= old_monkey:
                op_type, value = operations[new_monkey]
                pred = tests[new_monkey]
                inspected_items[new_monkey] += 1
                new_worry = apply_operation(op_type, value, old)
                old = (new_worry // worry_level_div) % (worry_level_div * modulo)
                old_monkey, new_monkey = new_monkey, pred[1 + (old % pred[0] != 0)]

    return prod(sorted(inspected_items)[-2:])
