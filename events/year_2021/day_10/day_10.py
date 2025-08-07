"""
Advent of Code - Year 2021 - Day 10
https://adventofcode.com/2021/day/10
"""


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Splits the input puzzle string into a list of lines.
    """
    return puzzle_input.splitlines()


def solver(lines: list[str]) -> tuple[int, int]:
    """
    Calculates the total syntax error score and the median completion score for a list of bracketed
    strings.
    """
    close = {'(': ')', '[': ']', '{': '}',  '<': '>'}
    score = {')': 3,   ']': 57,  '}': 1197, '>': 25137}
    table = {')': 1,   ']': 2,   '}': 3,    '>': 4}

    to_close = []
    syntax_error = 0
    completion_scores = set()

    for line in lines:
        for char in line:
            if char in close:
                to_close.append(close[char])
            elif char != to_close.pop():
                syntax_error += score[char]
                to_close = []
                break

        line_score = 0
        while to_close:
            line_score *= 5
            line_score += table[to_close.pop()]
        completion_scores.add(line_score)

    return (syntax_error,
            sorted(completion_scores)[len(completion_scores) // 2])
