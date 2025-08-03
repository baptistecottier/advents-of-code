"""
Advent of Code - Year 2020 - Day 23
https://adventofcode.com/2020/day/23
"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a string of digits into a list of integers.
    """
    return [int(item) - 1 for item in puzzle_input]


def solver(cups: list[int]) -> tuple[str, int]:
    """
    Solves a cup game puzzle by simulating moves and returning a string result and a product of two
    values after specific iterations.
    """
    updated_cups = move(cups, 100)
    curr = 0
    answer = ""
    while updated_cups[curr]:
        answer += str((curr := updated_cups[curr]) + 1)

    cups += list(range(max(cups) + 1, 1_000_000))
    updated_cups = move(cups, 10_000_000)
    return (answer,
            (updated_cups[0] + 1) * (updated_cups[updated_cups[0]] + 1))


def move(cups: list[int], steps: int) -> dict[int, int]:
    """
    Performs a series of cup moves according to a specific set of rules and returns the resulting
    cup mapping as a dictionary.
    """
    updated_cups = dict(zip(cups, cups[1:] + [cups[0]]))
    bound = len(cups)
    current = cups[0]

    for _ in range(steps):
        dest = (current - 1) % bound
        while dest in (a := updated_cups[current], b := updated_cups[a], c := updated_cups[b]):
            dest = (dest - 1) % bound

        updated_cups[current] = updated_cups[c]
        updated_cups[c] = updated_cups[dest]
        updated_cups[dest] = a
        current = updated_cups[current]

    return updated_cups
