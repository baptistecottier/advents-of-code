"""
Advent of Code - Year 2017 - Day 15
https://adventofcode.com/2017/day/15
"""


def preprocessing(puzzle_input: str) -> tuple[int, int]:
    """
    Extract both generators initial value

    Example:
        >>> preprocessing(Generator A starts with 65\nGenerator B starts with 8921)
        (65, 8921)
    """
    items = puzzle_input.split()
    return int(items[4]), int(items[9])


def solver(gen_a: int, gen_b: int) -> tuple[int, int]:
    """
    Simulates two pseudorandom number generators and counts matches in their outputs.

    Part 1: Counts matches in lower 16 bits over 40M iterations.
    Part 2: Counts matches between filtered values (gen_a divisible by 4, gen_b by 8).

    Args:
        gen_a: Starting seed for generator A
        gen_b: Starting seed for generator B

    Returns:
        tuple: (part1_matches, part2_matches)

    Example:
        >>> solver(65, 8921)
        (588, 309)
    """
    first_logic_count = 0
    to_hand_gen_a = []
    to_hand_gen_b = []
    mod = 2**16

    for _ in range(40_000_000):
        gen_a = (gen_a * 16_807) % 2_147_483_647
        gen_b = (gen_b * 48_271) % 2_147_483_647

        if (gen_a - gen_b) % mod == 0:
            first_logic_count += 1
        if gen_a % 4 == 0:
            to_hand_gen_a.append(gen_a % mod)
        if gen_b % 8 == 0:
            to_hand_gen_b.append(gen_b % mod)

    return (
        first_logic_count,
        sum(gen_a == gen_b for gen_a, gen_b in zip(to_hand_gen_a, to_hand_gen_b)),
    )
