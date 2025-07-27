"""
Advent of Code - Year 2018 - Day 9
https://adventofcode.com/2018/day/9
"""

from collections import defaultdict, deque
from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> tuple[int, int]:
    """
    Parse puzzle input to extract number of players and last marble value.
    """
    details = puzzle_input.split(' ')
    return (int(details[0]), int(details[-2]))


def solver(players: int, last_marble: int) -> Iterator[int]:
    """
    Solves marble circle game for given number of players and marbles.

    Uses deque for efficient circular operations. Yields high scores at marble
    milestones and final maximum score.

    Args:
        players: Number of players in the game
        last_marble: Last marble number to place

    Yields:
        int: Maximum score at last_marble+1 and final maximum score

    Example:
        >>> list(solver(9, 25))
        [32, 8317]
        >>> list(solver(10, 1618))
        [8317, 146373]
    """
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(100 * last_marble):
        if marble + 1 == last_marble:
            yield max(scores.values())

        if (marble + 1) % 23 == 0:
            circle.rotate(7)
            scores[(marble + 1) % players] += (marble + 1) + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble + 1)

    yield max(scores.values())
