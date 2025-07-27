"""
Advent of Code - Year 2018 - Day 7
https://adventofcode.com/2018/day/7
"""

from copy import deepcopy
from dataclasses import dataclass
from re import findall
from string import ascii_uppercase


@dataclass
class Worker:
    """
    Represents a worker that can process steps with a delay.
    """
    step: str
    delay: int


def preprocessing(puzzle_input: str) -> dict[str, set[str]]:
    """
    Parse puzzle input to extract step dependencies.

    Extracts uppercase letters from input text and builds a dictionary mapping
    each letter to its set of prerequisite steps.

    Args:
        puzzle_input (str): Raw input containing step dependency instructions

    Returns:
        dict: Dictionary where keys are steps (A-Z) and values are sets of
              prerequisite steps that must be completed first

    Example:
        >>> preprocessing("Step C must be finished before step A can begin.")
        {'A': {'C'}, 'B': set(), 'C': set(), ...}
    """
    instructions = {c: set() for c in ascii_uppercase}
    steps = findall(r'[A-Z]', puzzle_input)
    while steps:
        instructions[steps.pop()].add(steps.pop())
        steps.pop()
    return instructions


def solver(requirements: dict[str, set[str]]) -> tuple[str, int]:
    """
    Solve the step ordering puzzle for both parts.

    Args:
        requirements: Dict mapping steps to their prerequisite steps

    Returns:
        Generator yielding:
            - Part 1: String of steps in completion order with 1 worker
            - Part 2: Total time to complete all steps with 5 workers

    Examples:
        >>> reqs = {'B': ['A'], 'C': ['A'], 'D': ['B', 'C']}
        >>> results = list(solver(reqs))
        >>> results[0]  # Step order
        'ABCD'
        >>> results[1]  # Total time
        253
    """
    return (complete_steps(deepcopy(requirements), 1)[0],
            complete_steps(requirements, 5)[1])


def complete_steps(requirements: dict[str, set[str]], nb_workers: int) -> tuple[str, int]:
    """
    Simulate parallel execution of steps with worker constraints.

    Args:
        requirements: Dict mapping each step to its prerequisite steps
        nb_workers: Number of workers available to execute steps in parallel

    Returns:
        tuple: (completion_order, total_seconds)
            - completion_order: String of steps in order they were completed
            - total_seconds: Total time needed to complete all steps

    Example:
        >>> reqs = {'A': set(), 'B': {'A'}, 'C': {'A', 'B'}}
        >>> complete_steps(reqs, 2)
        ('ABC', 258)
    """
    started = []
    finished = []
    waiting = list(ascii_uppercase)
    workers = [Worker("", 0) for _ in range(nb_workers)]
    second = 0

    cnt = 0
    for step in ascii_uppercase:
        if requirements[step] <= set(finished) and cnt < nb_workers:
            started.append(step)
            cnt += 1

    while len(finished) != 26:
        update_available_steps(workers, waiting, started, finished, requirements)
        apply_steps(workers, waiting, started)
        second += 1

    return ''.join(finished), second - 1


def update_available_steps(
        workers: list[Worker],
        waiting: list[str],
        started: list[str],
        finished: list[str],
        requirements: dict[str, set[str]]) -> None:
    """
    Updates the available steps based on worker completion and dependency requirements.

    Processes completed worker steps, adds them to finished list, and moves eligible
    waiting steps to started list based on dependency satisfaction and worker capacity.

    Args:
        workers: List of worker objects with 'step' and 'delay' attributes
        waiting: List of steps waiting to be started
        started: List of steps that have been started (modified in-place)
        finished: List of completed steps (modified in-place)
        nb_workers: Maximum number of workers available
        requirements: Dict mapping steps to their required prerequisite steps
    """
    for worker in workers:
        cnt = 0
        if worker.step and not worker.delay:
            finished.append(worker.step)
            for step in waiting:
                if requirements[step] <= set(finished) and cnt < len(workers):
                    started.append(step)
                    cnt += 1


def apply_steps(
        workers: list[Worker],
        waiting: list[str],
        started: list[str]) -> None:
    """
    Advances worker simulation by one time step, assigning new tasks and decrementing delays.
    For each worker, if their delay reaches 0 and there are started tasks available,
    assigns the next task and sets the worker's delay based on the task character.
    All workers have their delay decremented by 1.
    Args:
        workers: List of Worker objects with delay attributes
        waiting: List of task strings waiting to be processed
        started: List of task strings ready to be assigned to workers
    """
    for i, worker in enumerate(workers):
        if worker.delay <= 0:
            if started:
                x = started.pop(0)
                waiting.remove(x)
                workers[i] = Worker(x, ord(x) - 5)
        worker.delay -= 1
