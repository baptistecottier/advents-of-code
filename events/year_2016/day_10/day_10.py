"""Advent of Code - Year 2016 - Day 10"""

from collections import defaultdict

def preprocessing(puzzle_input: str) -> tuple[dict, dict]:
    """
    Parse and process puzzle input to organize bot instructions and value assignments.

    The function processes two types of instructions:
    1. Value assignments: 'value N goes to bot X'
    2. Bot instructions: 'bot X gives low to [bot/output] Y and high to [bot/output] Z'

    Args:
        puzzle_input (str): Raw puzzle input containing bot instructions and value assignments

    Returns:
        tuple: Two dictionaries:
            - bots (dict): Maps bot IDs to their current values
            - gifts (dict): Maps bot IDs to tuples of (low_target, high_target) where:
                - Positive numbers represent bot targets
                - Negative numbers represent output targets (stored as -(output_number + 1))

    Example:
        >>> input = "value 5 goes to bot 2\\nbot 2 gives low to bot 1 and high to output 0"
        >>> bots, gifts = preprocessing(input)
        >>> bots[2]  # Contains [5]
        >>> gifts[2]  # Contains (1, -1)
    """
    bots  = defaultdict(list)
    gifts = defaultdict(tuple[int, int])

    for instruction in puzzle_input.splitlines():
        data = instruction.split()
        if data[0] == "value":
            bots[int(data[-1])].append(int(data[1]))
        else:
            low  = int(data[6])
            high = int(data[-1])
            if data[5]  == "output":
                low  = - (low + 1)
            if data[10] == "output":
                high = - (high + 1)
            gifts[int(data[1])] = (low, high)
    return bots, gifts


def solver(bots: dict, gifts: dict, chips_str: str = 'value-17, value-61'):
    """
    Simulates the distribution of microchips among bots according to specified rules and yields 
    results.

    Args:
        bots (dict): A dictionary mapping bot IDs to lists of microchips currently held by each bot.
        gifts (dict): A dictionary mapping bot IDs to a tuple (low, high) indicating the recipient 
            bot IDs for the lower and higher valued microchips, respectively.
        chips (str, optional): A comma-separated string of the two chip values to track (default is
            'value-17, value-61').

    Yields:
        int: The ID of the bot that compares the specified chip values.
        int: The product of the last three microchips distributed among the bots.

    Note:
        The function modifies the input 'bots' dictionary in place as it simulates the distribution.
    """
    chips = [int(item) for item in chips_str.replace("value-","").split(',')]
    while (to_distribute := [bot for bot in list(bots.items()) if len(bot[1]) == 2]):
        for bot, microchips in to_distribute:
            microchips.sort()
            if set(microchips) == set(chips):
                yield bot
            low, high = gifts[bot]
            bots[high].append(microchips.pop())
            bots[low].append(microchips.pop())
    yield bots[-1].pop() * bots[-2].pop() * bots[-3].pop()
