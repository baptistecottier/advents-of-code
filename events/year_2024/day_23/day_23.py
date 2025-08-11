"""
Advent of Code - Year 2024 - Day 23
https://adventofcode.com/2024/day/23
"""

from collections import defaultdict, deque
from itertools import combinations


def preprocessing(puzzle_input: str) -> tuple[set[str], dict[str, set[str]]]:
    """
    Parses the puzzle input into a set of computers and a dictionary of their connections.
    """
    computers = set()
    connections = defaultdict(set)
    for connection in puzzle_input.splitlines():
        a, b = connection.split('-')
        connections[a].add(b)
        connections[b].add(a)
        computers.update({a, b})
    return computers, connections


def solver(computers: set[str], connections: dict[str, set[str]]) -> tuple[int, str]:
    """
    Analyzes computer connections to count suspected LANs and find a maximal clique of connected
    computers.
    """
    suspected_lans = 0
    for a, b, c in combinations(computers, 3):
        if b in connections[a] and c in connections[a] and b in connections[c]:
            if any(n.startswith('t') for n in (a, b, c)):
                suspected_lans += 1

    queue = deque([[c] for c in computers])
    while len(queue) > 1:
        lan = queue.popleft()
        for computer in computers:
            if computer not in lan:
                if set(lan) <= connections[computer]:
                    queue.append(lan + [computer])
                    break

    return suspected_lans, ",".join(sorted(queue.pop()))
