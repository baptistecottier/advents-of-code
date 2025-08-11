"""
Advent of Code - Year 2024 - Day 7
https://adventofcode.com/2024/day/7
"""

from collections import deque
from collections.abc import Callable, Iterator
from copy import deepcopy
from operator import add, mul


def preprocessing(puzzle_input: str) -> list[tuple[int, list[int]]]:
    """
    Parses the puzzle input into a list of tuples containing an integer and a list of integers for
    each line.
    """
    equations = []

    for line in puzzle_input.splitlines():
        test_value, numbers = line.split(': ')
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        equations.append((test_value, numbers))

    return equations


def solver(equations: list[tuple[int, list[int]]]) -> Iterator[int]:
    """
    Yields calibration results for the given equations using different combinations of operations.
    """
    for available_op in [(add, mul), (add, mul, concat_int)]:
        yield get_calibration_result(deepcopy(equations), available_op)


def concat_int(a: int, b: int) -> int:
    """
    Given two integers a=(a_n...a_0) and b=(b_m...b_0), return a_n...a_0b_m...b_0
    """
    return int(f"{a}{b}")


def get_calibration_result(equations: list[tuple[int, list[int]]],
                           available_operations: tuple[Callable, ...]
                           ) -> int:
    r"""
    For each pair of test_value and numbers, we compute all combinations possible. of operators
    until one results in the test value. To avoid recomputing several times the same operation, we
    compute possibilities as a tree, where a branch is cut if the calibration result is greater
    than the test value.

    Consider the following example : 136 : 81 40 15
                81              We start with the first value
               /  \
    (40)      +    *            We compute the result for each available operation
             /       \          (here, addition and multiplication)
            121      3240       As all numbers are positive and operations increase
           /   \                the result, we cut the branch with the value 3240
    (15)  +     *               but we keep going for the left branch and compute
        /        \              the result for all operations. Using two additions
    136        1815             leads to the expected test value.
    """
    calibration_result = 0

    for test_value, numbers in equations:
        found = False
        candidates = deque([numbers.pop(0)])

        while numbers:
            b = numbers.pop(0)
            next_candidates = deque()

            while candidates and not found:
                result = candidates.pop()
                for f in available_operations:
                    temp = f(result, b)
                    if temp > test_value:
                        continue
                    if temp == test_value and numbers == []:
                        calibration_result += test_value
                        found = True
                        break
                    next_candidates.append(temp)

            candidates = next_candidates
    return calibration_result
