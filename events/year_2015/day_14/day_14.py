"""Advent of Code - Year 2015 - Day 14"""

from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Extract numerical values from puzzle input in groups of 3.

    Args:
        puzzle_input (list): Raw puzzle input

    Returns:
        list: List of list containing (speed, duration, rest) values

    Examples:
        >>> preprocessing(
            "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds."
            )
        [[14, 10, 127]]

        >>> preprocessing(
            "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.\\n
             Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
            )
        [[14, 10, 127], [16, 11, 162]]
    """
    return extract_chunks(puzzle_input, 3, neg=False)


def solver(reindeers_infos: list[list[int]], t: int = 2504) -> tuple[int, int]:
    """
    Calculate winning reindeer's distance and points in a race.

    Args:
        reindeers_infos (list[list[int]]): List of [speed, flight_duration, rest_duration]
        t (int, optional): Race duration in seconds. Defaults to 2504.

    Returns:
        tuple[int, int]: (max_distance, max_points)

    Examples:
        >>> solver([[14, 10, 127], [16, 11, 162]], 1000)
        (1120, 312)

        >>> solver([[14, 10, 127]], 1000)
        (1120, 1000)
    """
    bonus = [0 for _ in reindeers_infos]
    ranking = []
    for second in range(1, int(t)):
        ranking = []
        for speed, duration, rest in reindeers_infos:
            q = second // (duration + rest)
            r = min(duration, second % (duration + rest))
            ranking.append(speed * (r + q * duration))

        best = max(ranking)
        for i, rank in enumerate(ranking):
            if rank == best:
                bonus[i] += 1

    return max(ranking), max(bonus)
