"""Advent of Code - Year 2017 - Day 15"""

def preprocessing(puzzle_input: str) -> tuple[int, int]:
    """
    Extract both generators initial value
    
    Example:
        >>> preprocessing(Generator A starts with 65\nGenerator B starts with 8921)
        (65, 8921)
    """
    items = puzzle_input.split()
    return int(items[4]), int(items[9])


def solver(gen_a: int, gen_b: int):
    """
    Solves the puzzle by simulating two number generators and comparing their values.
    
    This function implements a dual-purpose simulation:
    1. For part 1: Counts matches in the lowest 16 bits of both generators for 40M iterations
    2. For part 2: Collects values that meet specific criteria and counts matches among them
    
    Args:
        gen_a: Initial seed value for generator A
        gen_b: Initial seed value for generator B
        
    Returns:
        tuple: (first_count, second_count) where:
            - first_count: Number of matches in the lowest 16 bits across all 40M iterations
            - second_count: Number of matches among values meeting the criteria (A divisible by 4,
              B divisible by 8)
    """
    first_logic_count = 0
    to_hand_gen_a = []
    to_hand_gen_b = []
    mod = 2 ** 16

    for _ in range(40_000_000):
        gen_a = (gen_a * 16_807) % 2_147_483_647
        gen_b = (gen_b * 48_271) % 2_147_483_647

        if (gen_a - gen_b) % mod == 0:
            first_logic_count += 1
        if gen_a % 4 == 0:
            to_hand_gen_a.append(gen_a % mod)
        if gen_b % 8 == 0:
            to_hand_gen_b.append(gen_b % mod)

    return (first_logic_count,
            sum(gen_a == gen_b for gen_a, gen_b in zip(to_hand_gen_a, to_hand_gen_b)))
