from itertools import combinations

def parser(data: str):
    return tuple(int(container) for container in data.splitlines())

def solver(containers: list[int]):
    fills: list[int] = list(sum(sum(comb) == 150 for comb in combinations(containers, size)) for size in range(len(containers)))
    fills = list(fill for fill in fills if fill)
    yield fills[0]
    yield sum(fills)