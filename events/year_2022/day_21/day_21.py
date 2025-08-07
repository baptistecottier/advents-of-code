"""
Advent of Code - Year 2022 - Day 21
https://adventofcode.com/2022/day/21
"""

from pythonfw.functions import sign


def preprocessing(puzzle_input: str) -> tuple[list[list[str]], str, str]:
    """
    Parses the puzzle input into a list of tokenized lines and extracts the left and right operands
    for the 'root' entry.
    """
    data = []
    left = right = ""
    for line in puzzle_input.replace(':', '').splitlines():
        details = line.split(' ')
        data.append(details)
        if details[0] == 'root':
            left, right = details[1], details[3]

    return data, left, right


def solver(monkeys: list[list[str]], left: str, right: str) -> tuple[int, int]:
    """
    Solves for the number yelled by the root monkey and finds the value of 'humn' that balances the
    root's output using binary search.
    """
    yelled_number_by_root_monkey = int(root_yell(monkeys, -1, left, right))

    min_bound, max_bound = 0, 1_000_000_000_000_000
    delta_humn = -1
    humn = 0

    while delta_humn != 0:
        humn = (min_bound + max_bound) // 2
        delta_humn = root_yell(monkeys, humn, left, right)

        delta_min_bound = root_yell(monkeys, min_bound, left, right)

        if delta_min_bound == delta_humn:
            min_bound = max_bound
        max_bound = humn

    return yelled_number_by_root_monkey, humn


def root_yell(mnks: list[list[str]], humn: int, left: str, right: str):
    """
    Evaluates a list of monkey operations and returns either the sum or the sign of the difference
    between two specified monkeys' values, depending on the presence of 'humn'.
    """
    monkeys = {}

    if humn != -1:
        monkeys['humn'] = humn

    while len(monkeys) != len(mnks):
        for details in mnks:
            v_out = details[0]
            v_in = details[1:]

            if monkeys.get(v_out) is None:
                if len(v_in) == 1:
                    monkeys[v_out] = int(v_in[0])
                elif all(monkeys.get(v_in[i]) is not None for i in [0, 2]):
                    a = monkeys[v_in[0]]
                    b = monkeys[v_in[2]]
                    match v_in[1]:
                        case '+': monkeys[v_out] = a + b
                        case '-': monkeys[v_out] = a - b
                        case '*': monkeys[v_out] = a * b
                        case '/': monkeys[v_out] = a / b

    if humn == -1:
        return monkeys[left] + monkeys[right]
    return sign(monkeys[left] - monkeys[right])
