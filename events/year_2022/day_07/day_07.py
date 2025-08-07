"""
Advent of Code - Year 2022 - Day 7
https://adventofcode.com/2022/day/7
"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Processes the puzzle input to compute and return a sorted list of folder sizes.
    """
    sizes = {}
    path = ["root"]

    for command in puzzle_input.splitlines():
        details = command.split(' ')
        match details:
            case ["$", "cd", "/"]: path = ["root"]
            case ["$", "cd", ".."]: path.pop()
            case ["$", "cd", _]: path.append("".join(path) + details[2])
            case ["dir", _]: pass
            case ["$", "ls"]: pass
            case _:
                for folder in path:
                    if folder in sizes:
                        sizes[folder] += int(details[0])
                    else:
                        sizes[folder] = int(details[0])

    return sorted(sizes.values())


def solver(sizes: list[int]) -> tuple[int, int]:
    """
    Yields the sum of sizes less than or equal to 100,000 and the first size greater than
    (root_size - 40,000,000) from the input list.
    """
    size = 0
    small_sizes = 0
    root_size = sizes.pop()

    for size in sizes:
        if size <= 100_000:
            small_sizes += size
        if size > (root_size - 40_000_000):
            break

    return small_sizes, size
