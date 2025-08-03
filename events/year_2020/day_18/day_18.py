"""
Advent of Code - Year 2020 - Day 18
https://adventofcode.com/2020/day/18
"""

from numexpr import evaluate


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Removes all spaces from each line of the input string and returns a list of the resulting
    strings.
    """
    return list(expr.replace(' ', '') for expr in puzzle_input.splitlines())


def solver(expressions: list[str]) -> tuple[int, int]:
    """
    Evaluates a list of arithmetic expressions using two different operator precedence rules and
    returns the sum of results for each rule.
    """
    return (sum(parse(expr) for expr in expressions),
            sum(int(evaluate("(" + expr.replace('*', ')*(') + ')+(0)')) for expr in expressions))


def pre_evaluate(expr: str) -> int:
    """
    Recursively evaluates a simple arithmetic expression string containing integers, addition, and
    multiplication, handling one operator at a time.
    """
    pos = -1

    for i, _ in enumerate(expr):
        if i >= len(expr):
            return pre_evaluate(expr)
        match (expr.count('*'), expr.count('+')):
            case (0, 0):
                return int(expr)
            case (1, 0):
                a, b = expr.split('*')
                return int(a) * int(b)
            case (0, 1):
                a, b = expr.split('+')
                return int(a) + int(b)

        if pos == -1:
            pos = i
            while list(expr)[i] not in '*+':
                i += 1
        else:
            while i < len(expr) and str(list(expr)[i]).isnumeric():
                i += 1
            expr = expr.replace(str(expr[pos:i]), str(pre_evaluate(expr[pos:i])), 1)
    raise ValueError("Oops... Something went wrong...")


def parse(expr: str) -> int:
    """
    Evaluates a mathematical expression string with parentheses and returns the computed integer
    result.
    """
    while True:
        total = l_br = r_br = 0
        if all(c not in expr for c in '()'):
            return pre_evaluate(expr)
        for i, c in enumerate(expr):
            if c == '(':
                l_br = i
            elif c == ')':
                r_br = i
                total = pre_evaluate(expr[l_br + 1: r_br])
                expr = expr.replace(str(expr[l_br: r_br + 1]), str(total), 1)
                break
