"""Advent of Code - Year 2016 - Day 21"""

from itertools import permutations


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Process the raw puzzle input by splitting into lines.

    Args:
        puzzle_input (str): Raw puzzle input string

    Returns:
        list[str]: List of input lines
    """
    return puzzle_input.splitlines()


def solver(operations: list[str], start: str = "abcdefgh"):
    """Solves puzzle by scrambling input string and finding original string that yields target.

    This function performs two operations:
    1. Scrambles the input string using given operations
    2. Finds the original string that when scrambled produces 'fbgdceah'

    Args:
        operations (list[str]): List of scrambling instructions to apply
        start (str, optional): Initial string to scramble. Defaults to "abcdefgh"

    Yields:
        str: First yields the scrambled result of start string
        str: Then yields the found original string that scrambles to 'fbgdceah'

    Example:
        >>> list(solver(['swap position 4 with position 0'], 'abcde'))
        ['ebcda']
    """
    yield scramble(list(start), operations)
    for word in permutations(start):
        if scramble(list(word), operations) == 'fbgdceah':
            yield ''.join(word)
            break


def scramble(pw: list, instructions: list[str]) -> str:
    """
    Scrambles a password string according to a list of instruction strings.

    Args:
        pw (str): The initial password to scramble.
        instructions (list[str]): List of instruction strings to apply.

    Returns:
        str: The scrambled password.
    """
    for inst in instructions:
        command , details = inst.split(' ', 1)
        match command:
            case 'swap':
                _, x, _, _, y = details.split(' ')
                if 'position' in details:
                    x, y = int(x), int(y)
                    pw[x], pw[y] = pw[y], pw[x]
                else:
                    pw = list((''.join(pw)).replace(x, '_').replace(y,x).replace('_',y))

            case 'rotate':
                if 'based' in details:
                    x    = pw.index(details[-1])
                    step = 1 + x + ( x >= 4 )
                else:
                    direction, x = details.split(' ')[:2]
                    if direction == 'right':
                        step = int(x)
                    else:
                        step = - int(x)
                temp = pw
                pw   = [temp[(i - step) % len(pw)] for i in range(len(pw))]

            case 'reverse':
                _ , x , _, y = details.split(' ')
                x , y = int(x), int(y)
                pw    = pw[:x] + pw[x: y + 1][::-1] + pw[y + 1:]

            case 'move':
                _, x, _, _, y = details.split(' ')
                x, y = int(x), int(y)
                t    = pw[x]
                pw   = pw[:x] + pw[x + 1:]
                pw   = pw[:y] + [t] + pw[y:]
    return ''.join(pw)
