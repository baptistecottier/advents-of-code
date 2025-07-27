"""
Advent of Code - Year 2016 - Day 10
https://adventofcode.com/2016/day/10
"""

from collections import defaultdict


def preprocessing(puzzle_input: str) -> tuple[dict, dict]:
    """
    Parse puzzle input to extract bot values and gift routing instructions.

    Args:
        puzzle_input: Multi-line string with 'value X goes to bot Y' and
                     'bot X gives low to bot/output Y and high to bot/output Z' instructions

    Returns:
        tuple: (bots dict with bot_id -> list of values,
                gifts dict with bot_id -> (low_target, high_target))
                Output targets are encoded as negative numbers: -(output_id + 1)
    """
    bots = defaultdict(list)
    gifts = defaultdict(tuple[int, int])

    for instruction in puzzle_input.splitlines():
        data = instruction.split()
        if data[0] == "value":
            bots[int(data[-1])].append(int(data[1]))
        else:
            low = int(data[6])
            high = int(data[-1])
            if data[5] == "output":
                low = -(low + 1)
            if data[10] == "output":
                high = -(high + 1)
            gifts[int(data[1])] = (low, high)
    return bots, gifts


def solver(bots: dict, gifts: dict, chips_str: str = "value-17, value-61") -> tuple[int, int]:
    """
    Simulates bot microchip distribution and finds specific bot and product calculation.

    Args:
        bots (dict): Dictionary mapping bot IDs to lists of microchips
        gifts (dict): Dictionary mapping bot IDs to (low_target, high_target) tuples
        chips_str (str): Comma-separated string of chip values to find (default: "value-17,
                                                                                  value-61")

    Returns:
        tuple: (bot_id_with_target_chips, product_of_last_three_bots)
    """
    bot_17_61 = -1
    chips = [int(item) for item in chips_str.replace("value-", "").split(",")]
    while to_distribute := [bot for bot in list(bots.items()) if len(bot[1]) == 2]:
        for bot, microchips in to_distribute:
            microchips.sort()
            if set(microchips) == set(chips):
                bot_17_61 = bot
            low, high = gifts[bot]
            bots[high].append(microchips.pop())
            bots[low].append(microchips.pop())
    return bot_17_61, bots[-1].pop() * bots[-2].pop() * bots[-3].pop()
