"""
Advent of Code - Year 2024 - Day 4
https://adventofcode.com/2024/day/4
"""


def preprocessing(puzzle_input: str) -> dict[str, set[tuple[int, int]]]:
    """
    Preprocessing consists in going through the puzzle input and stock position of the letters
    'X', 'M', 'A' and 'S'.
    """
    letters = {'X': set(), 'M': set(), 'A': set(), 'S': set()}

    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c in letters:
                letters[c].add((x, y))

    return letters


def solver(letters: dict[str, set[tuple[int, int]]]) -> tuple[int, int]:
    """
    Solves the puzzle by applying the find_xmas and find_x_mas functions to the given letters
    dictionary.
    """
    return find_xmas(letters), find_x_mas(letters)


def find_xmas(letters):
    """
    Patterns to be detected are:
    XMAS    X...    X...    ...X    SAMX    S...    S...    ...S
    ....    .M..    M...    ..M.    ....    .A..    A...    ..A.
    ....    ..A.    A...    .A..    ....    ..M.    M...    .M..
    ....    ...S    S...    S...    ....    ...X    X...    X...
    This function starts from every detected 'X' then check if a "MAS" is formed in any of the
    possible directions
    """
    cnt = 0
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    for (x, y) in letters['X']:
        cnt += sum(
            (x + dx, y + dy) in letters['M'] and
            (x + 2 * dx, y + 2 * dy) in letters['A'] and
            (x + 3 * dx, y + 3 * dy) in letters['S']
            for (dx, dy) in directions)

    return cnt


def find_x_mas(letters):
    """
    Patterns to be detected are:
    M.S     S.M     M.M     S.S
    .A.     .A.     .A.     .A.
    M.S     S.M     S.S     M.M

    Reading left-to-right, top-to-bottom without considering appearences of the letter 'A', the
    patterns are "MSMS", "SMSM", "MMSS" and "SSMM". This function therefore looks for this patterns
    around all 'A'.
    """
    cnt = 0
    patterns = ["MSMS", "SMSM", "MMSS", "SSMM"]

    for (x, y) in letters['A']:
        for (l1, l2, l3, l4) in patterns:
            top_left = (x - 1, y - 1) in letters[l1]
            top_right = (x + 1, y - 1) in letters[l2]
            bottom_left = (x - 1, y + 1) in letters[l3]
            bottom_right = (x + 1, y + 1) in letters[l4]
            if top_left and top_right and bottom_left and bottom_right:
                cnt += 1
                break

    return cnt
