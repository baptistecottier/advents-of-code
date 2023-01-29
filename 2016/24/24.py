from AoC_tools import bfs
from itertools import permutations, pairwise

def generator(input): return input.splitlines()

def part_1(input): return solver(input, round_trip = False)

def part_2(input): return solver(input, round_trip = True)

def solver(grid, round_trip):
	coordinates = [("".join(grid).index(str(i)) % len(grid[0]), "".join(grid).index(str(i)) // len(grid[0])) for i in range(8)]
	distances=[[bfs(grid, src, dst) for dst in coordinates] for src in coordinates]
	return min([sum([distances[start][end] for start, end in pairwise([0] + list(path) + round_trip * [0])]) for path in permutations(range(8))])
