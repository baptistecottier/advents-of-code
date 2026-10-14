# pylint: skip-file
# flake8: noqa
# type: ignore

"""
Advent of Code - Year 2023 - Day 25
https://adventofcode.com/2023/day/25
"""

from collections import defaultdict
from itertools import product
from random import choice


def preprocessing(puzzle_input):
    connections = defaultdict(list)
    for connection in puzzle_input.splitlines():
        lht, _rhts = connection.split(': ')
        rhts = _rhts.split(' ')
        connections[lht] += rhts
        for rht in rhts:
            connections[rht].append(lht)
    return connections


def solver(connections):
    nodes = list(connections)
    cnt_paths = {(n1, n2): 0 for n1, n2 in product(nodes, repeat = 2)}
    for _ in range(10):
        na = choice(nodes)
        nb = choice(nodes)
        path = get_path(na, nb, connections)
        for i in range(1, len(path)):
            cnt_paths[(min(path[i - 1], path[i]), max(path[i - 1], path[i]))] += 1
    to_remove = sorted(cnt_paths, key = lambda k: -cnt_paths[k])[:3]
    for na, nb in to_remove:
        connections[na].remove(nb)
        connections[nb].remove(na)

    start = nodes.pop()
    grp = {start}
    new = {start}
    nodes = set(nodes)
    visited = set()
    while new != set():
        news = new.copy()
        new = set()
        for n in news:
            for item in connections[n]:
                if item in visited:
                    continue
                visited.add(item)
                grp.add(item)
                new.add(item)
    yield len(grp) * len(nodes.difference(grp))
    


def get_path(start, end, connections):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        n = path[-1]
        if n == end:
            return path
        for nn in connections[n]:
            if nn in visited:
                continue
            visited.add(nn)
            queue.append(path + [nn])