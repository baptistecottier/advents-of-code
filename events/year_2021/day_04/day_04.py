"""
Advent of Code - Year 2021 - Day 4
https://adventofcode.com/2021/day/4
"""

from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input: str) -> tuple[list[int], list[list[int]]]:
    """
    Preprocesses the puzzle input into the draw sequence and list of boards.
    """
    draw, numbers = puzzle_input.split('\n\n', 1)
    draw = [int(number) for number in draw.split(',')]
    boards = extract_chunks(numbers, 25)
    return draw, boards


def solver(draw: list[int], boards: list[list[int]]) -> tuple[int, int]:
    """
    Yields the scores for the first winning board and the last losing board.
    """
    return first_win(draw.copy(), boards.copy()), last_lose(draw, boards)


def row_and_columns(board: list[int]) -> list[set[int]]:
    """
    Returns a list of sets representing all rows and columns of a bingo board.
    """
    return [set(board[5 * i: 5 * i + 5]) for i in range(5)] + [set(board[i:: 5]) for i in range(5)]


def first_win(draw: list[int], boards: list[list[int]]) -> int:
    """
    Returns the score of the first board to win in a bingo game given the draw sequence and list of
    boards.
    """
    drew = set(draw[:5])
    while True:
        ball = draw.pop(0)
        drew.add(ball)
        for board in boards:
            if any(line < drew for line in row_and_columns(board)):
                return ball * (sum(n for n in board if n not in drew))


def last_lose(draw: list[int], boards: list[list[int]]) -> int:
    """
    Returns the score of the last board to lose in a bingo game given the draw sequence and list of
    boards.
    """
    while ball := draw.pop():
        for board in boards:
            if all(not line < set(draw) for line in row_and_columns(board)):
                return ball * (sum(n for n in board if n not in draw) - ball)
    return 0
