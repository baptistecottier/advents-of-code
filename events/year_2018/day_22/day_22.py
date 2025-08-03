# """
# Advent of Code - Year 2018 - Day 22
# https://adventofcode.com/2018/day/22
# """

# import collections


# def preprocessing(puzzle_input: str) -> tuple[list[list[int]], int, int]:
#     """
#     Parses puzzle input to calculate erosion levels for a cave system and returns the erosion grid
#     with target coordinates.
#     """
#     depth, target = puzzle_input.splitlines()
#     depth = int(depth.rsplit(' ')[1])
#     tx, ty = tuple(int(n) for n in (target.split(': ')[1]).split(','))
#     line = [0]

#     for x in range(1, tx + 50):
#         line.append((x * 16807 + depth) % 20183)
#     erosion = [line]

#     for y in range(1, ty + 50):
#         line = [(y * 48271 + depth) % 20183]
#         for x in range(1, tx + 50):
#             line.append((line[x - 1] * erosion[y - 1][x] + depth) % 20183)
#         erosion.append(line)

#     erosion = [[item % 3 for item in y] for y in erosion]
#     erosion[ty][tx] = 0
#     return erosion, tx, ty


# def solver(erosion: list[list[int]], tx: int, ty: int):
#     """
#     Calculates the sum of erosion values within a rectangular region and returns it with a
#     placeholder message.
#     """
#     bfs(erosion, (0, 0), (tx, ty))
#     return sum(sum(y[:tx + 1]) for y in erosion[:ty + 1]), "To optimise"


# def bfs(maze: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
#     """
#     Finds the shortest path through a maze from start to end using breadth-first search with tool
#     switching mechanics.

#     Args:
#         maze (list[list[int]]): 2D grid representing the maze with terrain types (0, 1, 2)
#         start (tuple[int, int]): Starting coordinates (x, y)
#         end (tuple[int, int]): Target coordinates (x, y)

#     Returns:
#         int: Minimum time required to reach the end position with the correct tool
#     """
#     width, height = len(maze[0]), len(maze)
#     queue = collections.deque([[(*start, 0, 2)]])
#     seen = set([(0, 0, 2)])
#     test = set()
#     while queue:
#         path = queue.popleft()
#         x, y, delay, tool = path[-1]
#         if delay > 0:
#             queue.append(path + [(x, y, delay - 1, tool)])
#             continue

#         seen.add((x, y, tool))
#         if (x, y) == end:
#             if tool == 2:
#                 if delay == 0:
#                     return len(path)
#                 queue.append(path + [(x, y, delay - 1, 2)])
#             else:
#                 queue.append(path + [(x, y, 7, 2)])

#         else:
#             current_type = maze[y][x]
#             for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
#                 if 0 <= x2 < width and 0 <= y2 < height and (x2, y2, tool) not in seen:
#                     next_type = maze[y2][x2]
#                     match current_type, next_type:
#                         case 0, 0:
#                             queue.append(path + [(x2, y2, 0, tool)])
#                         case 1, 1:
#                             queue.append(path + [(x2, y2, 0, tool)])
#                         case 2, 2:
#                             queue.append(path + [(x2, y2, 0, tool)])
#                         case 0, 1:
#                             if tool == 1:
#                                 queue.append(path + [(x2, y2, 0, 1)])
#                             elif tool == 2:
#                                 queue.append(path + [(x2, y2, 6, 1)])
#                                 queue.append(path + [(x2, y2, 6, 0)])
#                         case 0, 2:
#                             if tool == 1:
#                                 queue.append(path + [(x2, y2, 6, 2)])
#                                 queue.append(path + [(x2, y2, 6, 0)])
#                             elif tool == 2:
#                                 queue.append(path + [(x2, y2, 0, 2)])
#                         case 1, 0:
#                             if tool == 1:
#                                 queue.append(path + [(x2, y2, 0, 1)])
#                             elif tool == 0:
#                                 queue.append(path + [(x2, y2, 6, 1)])
#                                 queue.append(path + [(x2, y2, 6, 2)])
#                         case 1, 2:
#                             if tool == 0:
#                                 queue.append(path + [(x2, y2, 0, 0)])
#                             elif tool == 1:
#                                 queue.append(path + [(x2, y2, 6, 0)])
#                                 queue.append(path + [(x2, y2, 6, 2)])
#                         case 2, 0:
#                             if tool == 2:
#                                 queue.append(path + [(x2, y2, 0, 2)])
#                                 seen.add((x2, y2, 2))
#                             elif tool == 0:
#                                 queue.append(path + [(x2, y2, 6, 2)])
#                                 queue.append(path + [(x2, y2, 6, 1)])
#                         case 2, 1:
#                             if tool == 2:
#                                 queue.append(path + [(x2, y2, 6, 0)])
#                                 queue.append(path + [(x2, y2, 6, 1)])
#                             elif tool == 0:
#                                 queue.append(path + [(x2, y2, 0, 0)])
#                                 seen.add((x2, y2, 0))
#     return min(test)
