"""
Advent of Code - Year 2024 - Day 21
https://adventofcode.com/2024/day/21
"""

from itertools import pairwise
from collections import defaultdict
from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[tuple[int, dict[str, int]]]:
    """
    Parses the puzzle input into a list of tuples containing an integer code and a dictionary of
    button transition counts.
    """
    numpad = {'7': (0, 0), '8': (1, 0), '9': (2, 0),
              '4': (0, 1), '5': (1, 1), '6': (2, 1),
              '1': (0, 2), '2': (1, 2), '3': (2, 2),
                           '0': (1, 3), 'A': (2, 3)}
    codes = []

    for raw_code in puzzle_input.splitlines():
        code = [(2, 3)] + [numpad[c] for c in raw_code]
        buttons = "A"

        for (xa, ya), (xb, yb) in pairwise(code):
            (dx, dy) = (xb - xa, yb - ya)
            padding = (dy * "v") + (-dy * "^") + (dx * ">") + (-dx * "<")
            if any(((dx > 0 and dy > 0 and (xa, yb) == (0, 3)),
                    (dx < 0 and dy < 0 and (xb, ya) != (0, 3)))):
                buttons += padding[::-1] + "A"
            else:
                buttons += padding + "A"

        dict_buttons = defaultdict(int)
        for i in range(len(buttons)-1):
            dict_buttons[buttons[i: i+2]] += 1
        codes.append((int(raw_code[:-1]), dict_buttons))

    return codes


def solver(codes_buttons: list[tuple[int, dict[str, int]]]) -> Iterator[int]:
    """
    Yields the result of count_presses for the given codes_buttons with 2 and 25 robots.
    """
    for n_robots in [2, 25]:
        yield count_presses(codes_buttons, n_robots)


def count_presses(buttons: list[tuple[int, dict[str, int]]], n_robots: int) -> int:
    """
    Calculates the total complexity by simulating button presses for each robot and summing the
    results.
    """
    complexity = 0
    for n, button in buttons:
        for _ in range(n_robots):
            button = get_presses(button)
        complexity += n * sum(button.values())
    return complexity


def get_presses(buttons: dict[str, int]) -> dict[str, int]:
    """
    Aggregates button press counts by mapping input button pairs to their corresponding press steps.
    """
    presses = {
        "<>": ["A>", ">>", ">A"],       "<v": ["A>", ">A"],
        "<^": ["A>", ">^", "^A"],       "<A": ["A>", ">>", ">^", "^A"],
        "><": ["A<", "<<", "<A"],       ">v": ["A<", "<A"],
        ">^": ["A<", "<^", "^A"],       ">A": ["A^", "^A"],
        "v<": ["A<", "<A"],             "v>": ["A>", ">A"],
        "v^": ["A^", "^A"],             "vA": ["A^", "^>", ">A"],
        "^<": ["Av", "v<", "<A"],       "^>": ["Av", "v>", ">A"],
        "^v": ["Av", "vA"],             "^A": ["A>", ">A"],
        "A<": ["Av", "v<", "<<", "<A"], "A>": ["Av", "vA"],
        "Av": ["A<", "<v", "vA"],       "A^": ["A<", "<A"],
        "<<": ["AA"],                   ">>": ["AA"],
        "vv": ["AA"],                   "^^": ["AA"],
        "AA": ["AA"]
        }
    dir_presses = defaultdict(int)
    for pair, occurences in buttons.items():
        for step in presses[pair]:
            dir_presses[step] += occurences
    return dir_presses
