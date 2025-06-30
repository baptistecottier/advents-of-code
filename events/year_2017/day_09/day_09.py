"""Advent of Code - Year 2017 - Day 09"""

from re import sub


def preprocessing(puzzle_input: str) -> str:
    """
    Remove exclamation marks and their following character from the puzzle input
    
    Example:
    -------
    >>> preprocessing("a!bc!d")
    'ac'
    """
    return sub(r'\!.', '', puzzle_input)


def solver(record: str):
    """
    Processes a stream of characters to compute group scores and count garbage characters.
    
    The function iterates through each character in the input record and, based on the 
    current state and character encountered, updates scores and counts.
    
    Rules:
    - '{' opens a group, incrementing the score by the current step value plus 1
    - '}' closes a group, decrementing the step counter
    - '<' begins a garbage section
    - '>' ends a garbage section
    - Characters inside garbage sections are counted
    
    Args:
        record: A string containing groups delimited by {} and garbage delimited by <>
        
    Returns:
        tuple: (total_score, garbage_count)
            - total_score: The sum of scores for all groups
            - garbage_count: The total number of characters inside garbage sections
    """
    step       = 0
    score      = 0
    garbage    = 0
    garb_count = 0

    for char in record:
        match (garbage, char):
            case (1, '>'): garbage = 0
            case (0, '<'): garbage = 1
            case (0, '{'): score, step = score + step + 1, step + 1
            case (0, '}'): step = step - 1
            case (0, _): pass
            case _: garb_count += 1

    return score, garb_count
