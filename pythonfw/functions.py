"""
Some tool-functions repeatedly used in advent of code
"""

# Standard imports
from collections import deque
from collections.abc import Callable
from inspect import currentframe, getouterframes
from functools import lru_cache
from math import lcm
from operator import gt
from re import findall

# Third-party import
import _md5


def upload_example():
    """
    Upload and read the example input file for the current script.

    Returns:
        str: The contents of the input file as a string.
    """
    path = getouterframes(currentframe(), 2)[1][1][:-3]
    with open(f"{path}.input", 'r', encoding="utf-8") as f:
        return f.read()


def bfs(
        maze: set,
        start: tuple,
        end: tuple,
        max_length: int = 1_000,
        predicate_arg: Callable | None = None) -> int:
    """
    Perform breadth-first search to find the shortest path in a maze.

    Args:
        maze: The maze data structure to search in
        start: Starting position as (x, y) tuple
        end: Target position as (x, y) tuple
        max_length: Maximum allowed path length (default 1000)
        predicate: Optional function to validate moves, defaults to checking if position is in maze

    Returns:
        int: Length of shortest path, or -1 if no path found or path exceeds max_length
    """
    if predicate_arg is None:
        def predicate(_pos, new, maze):
            return new in maze
    else:
        predicate = predicate_arg

    queue = deque([[start]])
    seen = set([start])

    while queue:
        path = queue.popleft()
        if len(path) > 1 + max_length:
            return -1
        x, y = path[-1]
        if (x, y) == end:
            return len(path)-1
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (x2, y2) not in seen and predicate((x, y), (x2, y2), maze):
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return -1


def chinese_remainder(
        equations: set[tuple[int, int]],
        get_modulo: bool = False) -> tuple[int, int]:
    """
    Solves a system of congruences using the Chinese Remainder Theorem.

    Args:
        equations: List of tuples (remainder, modulo) representing congruences
                   x ≡ remainder (mod modulo)
        get_modulo: If True, returns the modulo along with the solution

    Returns:
        Tuple containing (solution, modulo) where solution is the smallest non-negative integer
        satisfying all congruences. If get_modulo is False, modulo is 0.

    Examples:
        >>> chinese_remainder([(2, 3), (3, 5), (2, 7)])
        (23, 0)
        >>> chinese_remainder([(1, 2), (2, 3)], get_modulo=True)
        (5, 6)
    """
    solution = 0
    product = lcm(*(modulo for _, modulo in equations))
    for remainder, modulo in equations:
        sub_product = product // modulo
        solution += remainder * pow(sub_product, -1, modulo) * sub_product
    if get_modulo:
        return (solution % product, product)
    return (solution % product, 0)


def dijkstra(
        map_dict: dict[tuple[int, int], int],
        end_coords: tuple[int, int]) -> int:
    """
    Find the shortest path from (0, 0) to end_coords using Dijkstra's algorithm.

    Args:
        map_dict: Dictionary mapping coordinates to risk/weight values
        end_coords: Target coordinates as (x, y) tuple

    Returns:
        int: Minimum total risk/cost to reach the end coordinates
    """
    unvisited = set(map_dict.keys())
    node_dict = {(0, 0): 0}
    current_node = (0, 0)

    while current_node != end_coords:
        x, y = current_node
        neighbours = {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)}
        risk = node_dict[current_node]

        for next_to in [item for item in neighbours if item in unvisited]:
            current_risk = node_dict.get(next_to, None)
            new_risk = risk + map_dict[next_to]
            if not current_risk or new_risk < current_risk:
                node_dict[next_to] = new_risk

        unvisited.remove(current_node)
        del node_dict[current_node]

        lowest_risk = min(node_dict.values())
        for coords, risk in node_dict.items():
            if risk == lowest_risk:
                current_node = coords
                break

    return node_dict[end_coords]


def extract_chunks(
        data: str,
        take: int,
        skip: int = 0,
        neg: bool = True,
        func: Callable = lambda x: x) -> list[list[int]]:
    """
    Extract chunks of numbers from a string and apply a function to each chunk.

    Args:
        data (str): Input string containing numbers to extract
        take (int): Number of consecutive numbers to take in each chunk
        skip (int, optional): Number of numbers to skip between chunks. Defaults to 0.
        neg (bool, optional): Whether to include negative numbers. Defaults to True.
        func (Callable, optional): Function to apply to each chunk. Defaults to lambda x: x.

    Returns:
        list: List of processed chunks after applying the function to each chunk.
    """
    numbers = list(map(int, findall(r'[-]?[0-9]+' if neg else r'[0-9]+', data)))
    return list(func(numbers[i: i + take]) for i in range(0, len(numbers), take + skip))


def manhattan(pt1, pt2):
    """Calculate Manhattan distance between two points."""
    x1, y1 = pt1
    x2, y2 = pt2
    return abs(x1 - x2) + abs(y1 - y2)


@lru_cache
def md5(to_hash: str) -> str:
    """Compute MD5 hash of a string and return hexadecimal digest.
    Args:
        to_hash: String to hash
    Returns:
        Hexadecimal MD5 digest
    Examples:
        >>> md5("hello")
        '5d41402abc4b2a76b9719d911017c592'
        >>> md5("")
        'd41d8cd98f00b204e9800998ecf8427e'
    """
    return _md5.md5(to_hash.encode()).hexdigest()


def screen_reader(screen: set) -> str:
    """
    Converts a set of screen coordinates to readable text by parsing letter patterns.

    Args:
        screen (set): Set of (x, y) coordinate tuples representing lit pixels

    Returns:
        str: Decoded text string from the screen coordinates

    Raises:
        ValueError: If screen height is not 6 or 10 pixels
    """
    lx, ly = zip(*screen)
    mx = min(lx)
    my = min(ly)
    h = max(ly) - min(ly) + 1
    if h not in {6, 10}:
        raise ValueError("Screenn height must be 6 or 10")
    letter_width = {6: 5, 10: 8}
    w = letter_width[h]
    screen = {(x - mx, y - my) for (x, y) in screen}
    word = ''
    letters = [set() for _ in range(1 + max(x for (x, _) in screen) // w)]
    for (x, y) in screen:
        letters[x // w].add((x % w, y))
    for letter in letters:
        word += coords_to_letter(letter, h)
    return word


def sign(a: int, b: int = 0, f: Callable = gt) -> int:
    """
    Returns the sign of (a - b) based on comparison function f.

    Args:
        a: First value to compare
        b: Second value to compare (default: 0)
        f: Comparison function (default: gt for greater than)

    Returns:
        int: -1 if b > a, 1 if a > b, 0 if a == b

    Examples:
        >>> sign(5, 3)
        1
        >>> sign(2, 7)
        -1
        >>> sign(4, 4)
        0
        >>> sign(-3)
        -1
    """
    if f(b, a):
        return -1
    if f(a, b):
        return 1
    return 0


def coords_to_letter(coords: set, h: int) -> str:
    """
    Convert a set of coordinates to a letter based on pattern matching.

    Args:
        coords: Set of (x, y) coordinate tuples representing filled positions
        w: Width of the grid
        h: Height of the grid (6 or 10)

    Returns:
        Single character string representing the detected letter

    Examples:
        >>> coords_to_letter({(0,0), (0,1), (0,2), (0,3), (0,4), (0,5)}, 4, 6)
        'L'
        >>> coords_to_letter({(0,0), (1,0), (2,0), (3,0)}, 4, 6)
        'Z'
    """
    if h == 6:
        return _coords_to_letter_h6(coords)

    if h == 10:
        return _coords_to_letter_h10(coords)

    return ""


def _coords_to_letter_h6(coords: set) -> str:
    """
    Convert a set of coordinates to a corresponding letter character.

    Args:
        coords (set): Set of (x, y) coordinate tuples representing filled positions
        w (int): Width of the grid

    Returns:
        str: Single letter character (A-Z) based on coordinate pattern

    Raises:
        ValueError: If coordinate pattern doesn't match any recognized letter
    """
    def _coords_to_letter_h6_l9(coords):
        if any(x == 4 for (x, y) in coords):
            return 'Y'
        if all((0, y) in coords for y in range(6)):
            return 'L'
        return 'J'

    def _coords_to_letter_h6_l11(coords):
        if all((0, y) in coords for y in range(6)):
            return 'F'
        return 'S'

    def _coords_to_letter_h6_l12(coords):
        if all((x, 0) in coords for x in range(4)):
            return 'Z'
        if all((3 - y, y) in coords for y in range(4)):
            return 'K'
        if all((0, y) in coords for y in range(6)):
            return 'P'
        if all((0, y) in coords for y in range(5)):
            return 'U'
        return 'O'

    def _coords_to_letter_h6_l14(coords):
        if all((3, y) in coords for y in range(6)):
            return 'H'
        if all((x, x + 2) in coords for x in range(4)):
            return 'R'
        if all((0, y) in coords for y in range(6)):
            return 'E'
        return 'A'

    letter = ""
    match len(coords):
        case 9:  letter = _coords_to_letter_h6_l9(coords)
        case 10: letter = 'C'
        case 11: letter = _coords_to_letter_h6_l11(coords)
        case 12: letter = _coords_to_letter_h6_l12(coords)
        case 13: letter = 'G'
        case 14: letter = _coords_to_letter_h6_l14(coords)
        case 15: letter = 'B'

    if letter == "":
        raise ValueError("Letter not recognised!")
    return letter


def _coords_to_letter_h10(coords) -> str:
    letter = ""
    match len(coords):
        case 15: letter = 'L'
        case 16: letter = 'J'
        case 18: letter = 'C'
        case 21: letter = 'P'
        case 19: letter = 'F'
        case 20:
            if (0, 1) not in coords:
                letter = 'Z'
            elif (0, 2) in coords:
                letter = 'K'
            else:
                letter = 'X'
        case 24:
            if (1, 5) in coords:
                letter = 'A'
            elif (0, 0) not in coords:
                letter = 'G'
            elif (1, 0) in coords:
                letter = 'E'
            else:
                letter = 'H'
        case 26:
            letter = 'R'
        case 28:
            letter = 'N'
        case 29:
            letter = 'B'

    if letter == "":
        raise ValueError("Letter not recognised!")
    return letter


# ## HELPER FOR OCR

# h = 6
# A: [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 3), (2, 0), (2, 3), (3, 1), (3, 2),
#     (3, 3), (3, 4), (3, 5)]
# B: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 2), (1, 5), (2, 0), (2, 2),
#     (2, 5), (3, 1), (3, 3), (3, 4)]
# C: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 5), (2, 0), (2, 5), (3, 1), (3, 4)]
# D: Not encountered yet
# E: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 2), (1, 5), (2, 0), (2, 2),
#     (2, 5), (3, 0), (3, 5)]
# F: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 2), (2, 0), (2, 2), (3, 0)]
# G: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 5), (2, 0), (2, 3), (2, 5), (3, 1), (3, 3),
#     (3, 4), (3, 5)]
# H: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (2, 2), (3, 0), (3, 1), (3, 2),
#     (3, 3), (3, 4), (3, 5)]
# I: [(1, 0), (1, 5), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 0), (3, 5)]
# J: [(0, 4), (1, 5), (2, 0), (2, 5), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
# K: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (2, 1), (2, 3), (2, 4), (3, 0),
#     (3, 5)]
# L: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5)]
# M: Not encountered yet
# N: Not encountered yet
# O: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 5), (2, 0), (2, 5), (3, 1), (3, 2), (3, 3),
#     (3, 4)]
# P: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 3), (2, 0), (2, 3), (3, 1),
#     (3, 2)]
# Q: Not encountered yet
# R: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 3), (2, 0), (2, 3), (2, 4),
#     (3, 1), (3, 2), (3, 5)]
# S: [(0, 1), (0, 2), (0, 5), (1, 0), (1, 3), (1, 5), (2, 0), (2, 3), (2, 5), (3, 0), (3, 4)]
# T: Not encountered yet
# U: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (2, 5), (3, 0), (3, 1), (3, 2), (3, 3),
#     (3, 4)]
# V: Not encountered yet
# W: Not encountered yet
# X: Not encountered yet
# Y: [(2, 5), (0, 1), (2, 4), (1, 2), (0, 0), (3, 2), (4, 1), (2, 3), (4, 0)]
# Z: [(0, 0), (0, 4), (0, 5), (1, 0), (1, 3), (1, 5), (2, 0), (2, 2), (2, 5), (3, 0), (3, 1),
#     (3, 5)]

# h = 10
# A: (24, [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 1), (1, 5), (2, 0),
#          (2, 5), (3, 0), (3, 5), (4, 1), (4, 5), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7),
#          (5, 8), (5, 9)])
# B: (29, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0),
#          (1, 4), (1, 9), (2, 0), (2, 4), (2, 9), (3, 0), (3, 4), (3, 9), (4, 0), (4, 4), (4, 9),
#          (5, 1), (5, 2), (5, 3), (5, 5), (5, 6), (5, 7), (5, 8)])
# C: (18, [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 9), (2, 0),
#          (2, 9), (3, 0), (3, 9), (4, 0), (4, 9), (5, 1), (5, 8)])
# D: Not encountered yet
# E: (24, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0),
#          (1, 4), (1, 9), (2, 0), (2, 4), (2, 9), (3, 0), (3, 4), (3, 9), (4, 0), (4, 4), (4, 9),
#          (5, 0), (5, 9)])
# F: (19, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0),
#          (1, 4), (2, 0), (2, 4), (3, 0), (3, 4), (4, 0), (4, 4), (5, 0)])
# G: (24, [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 9), (2, 0),
#          (2, 9), (3, 0), (3, 5), (3, 9), (4, 0), (4, 5), (4, 8), (5, 1), (5, 5), (5, 6), (5, 7),
#          (5, 8), (5, 9)])
# H: (24, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 4),
#          (2, 4), (3, 4), (4, 4), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7),
#          (5, 8), (5, 9)])
# I: Not encountered yet
# J: (16, [(0, 7), (0, 8), (1, 9), (2, 9), (3, 0), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
#          (4, 5), (4, 6), (4, 7), (4, 8), (5, 0)])
# K: (20, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 4),
#          (1, 5), (2, 3), (2, 6), (3, 2), (3, 7), (4, 1), (4, 8), (5, 0), (5, 9)])
# L: (15, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 9),
#          (2, 9), (3, 9), (4, 9), (5, 9)])
# M: Not encountered yet
# N: (28, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 1),
#          (1, 2), (2, 3), (2, 4), (3, 5), (3, 6), (4, 7), (4, 8), (5, 0), (5, 1), (5, 2), (5, 3),
#          (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9)])
# O: Not encountered yet
# P: (21, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0),
#          (1, 4), (2, 0), (2, 4), (3, 0), (3, 4), (4, 0), (4, 4), (5, 1), (5, 2), (5, 3)])
# Q: Not encountered yet
# R: (26, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0),
#          (1, 4), (2, 0), (2, 4), (3, 0), (3, 4), (3, 5), (4, 0), (4, 4), (4, 6), (4, 7), (5, 1),
#          (5, 2), (5, 3), (5, 8), (5, 9)])
# S: Not encountered yet
# T: Not encountered yet
# U: Not encountered yet
# V: Not encountered yet
# W: Not encountered yet
# X: (20, [(0, 0), (0, 1), (0, 8), (0, 9), (1, 2), (1, 3), (1, 6), (1, 7), (2, 4), (2, 5), (3, 4),
#          (3, 5), (4, 2), (4, 3), (4, 6), (4, 7), (5, 0), (5, 1), (5, 8), (5, 9)])
# Y: Not encountered yet
# Z: (20, [(0, 0), (0, 7), (0, 8), (0, 9), (1, 0), (1, 6), (1, 9), (2, 0), (2, 5), (2, 9), (3, 0),
#          (3, 4), (3, 9), (4, 0), (4, 3), (4, 9), (5, 0), (5, 1), (5, 2), (5, 9)])
