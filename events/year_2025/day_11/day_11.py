"""
Advent of Code - Year 2025 - Day 11
https://adventofcode.com/2025/day/11
"""


from collections import deque, defaultdict


def preprocessing(puzzle_input: str) -> list[tuple[int, int]]:
    """
    Parse puzzle input to extract network connections and return them as a list of edges.
    """
    edges = []
    for line in puzzle_input.splitlines():
        ports = line.split()
        for to in ports[1:]:
            edges.append((ports[0][:-1], to))
    return edges


def solver(edge_list: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Solves a graph path-counting problem by first performing topological sorting on the input edge
    list. Calculates the number of paths from 'you' to 'out' for the first part of the solution.
    For the second part, uses conditional logic to count paths between specific nodes ('fft',
    'dac', 'svr', 'out'). 
    
    As the graph is non-cyclic, if no direct path exists from 'fft' to 'dac', it means the path to
    follow is 'svr' -> 'dac' -> 'fft' -> 'out'. Otherwise, it multiplies path counts from 'svr' to
    'fft' and from 'dac' to 'out'.
    
    Returns both results as a tuple of integers.
    """
    sorted_graph = topological_sort(edge_list)
    n_paths_from_you_to_out = count_paths(sorted_graph, 'you', 'out')
    n_paths = count_paths(sorted_graph, 'fft', 'dac')

    if n_paths == 0:
        n_paths += count_paths(sorted_graph, 'svr', 'dac')
        n_paths *= count_paths(sorted_graph, 'dac', 'fft')
        n_paths *= count_paths(sorted_graph, 'fft', 'out')
    else:
        n_paths *= count_paths(sorted_graph, 'svr', 'fft')
        n_paths *= count_paths(sorted_graph, 'dac', 'out')

    return n_paths_from_you_to_out, n_paths


def topological_sort(edge_list: list[tuple[int, int]]):
    """
    Performs topological sorting on a directed graph using Kahn's algorithm.
    """
    ports = set([u for u, _ in edge_list] + ['out'])
    graph = defaultdict(list)
    indegree = {p: 0 for p in ports}

    for u, v in edge_list:
        print(indegree)
        graph[u].append(v)
        indegree[v] += 1

    queue = deque()
    for i in ports:
        if indegree[i] == 0:
            queue.append(i)

    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append((node, graph[node]))

        for neighbor in graph[node]:
            if indegree[neighbor] == 1:
                queue.append(neighbor)
            indegree[neighbor] -= 1

    return topo_order


def count_paths(topo_order, source, destination):
    """
    Count the number of paths from source to destination in a topologically ordered DAG.
    """
    ways = defaultdict(int)
    ways[source] = 1

    for node, neighbors in topo_order:
        for neighbor in neighbors:
            ways[neighbor] += ways[node]

    return ways[destination]