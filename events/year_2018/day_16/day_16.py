"""
Advent of Code - Year 2018 - Day 16
https://adventofcode.com/2018/day/16
"""

# Standards imports
from copy import deepcopy

# First-party imports
from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input: str) -> tuple[list[list[list[int]]], list[list[int]]]:
    """
    Parses puzzle input into samples and tests by splitting on quadruple newlines and extracting
    chunks.
    """
    samples, tests = puzzle_input.split('\n\n\n\n')
    samples = [[sample[:4], sample[4:8], sample[8:]] for sample in extract_chunks(samples, 12)]
    tests = extract_chunks(tests, 4)
    return samples, tests


def solver(samples: list[list[list[int]]], tests: list[list[int]]):
    """
    Solves a puzzle by analyzing opcode samples to determine valid operations and executing test
    instructions.
    """
    good_samples = 0
    matches = {s: {c: 0 for c in range(16)} for s in range(16)}

    for before, instruction, after in samples:
        real_opcode = instruction[0]
        good_opcodes = 0
        for opcode in range(16):
            instruction[0] = opcode
            if after == apply_opcode(instruction, deepcopy(before)):
                good_opcodes += 1
                matches[real_opcode][opcode] += 1
        if good_opcodes >= 3:
            good_samples += 1
    yield good_samples

    matches = {
        s:
        {c: n for c, n in matches[s].items() if n == max(matches[s].values())}
        for s in range(16)
        }
    perm = [-1 for _ in range(16)]

    while -1 in perm:
        for opcode, candidates in matches.items():
            if len(candidates) == 1:
                perm_oc = candidates.popitem()[0]
                perm[perm_oc] = opcode
                del matches[opcode]
                for opcode, candidates in matches.items():
                    candidates.pop(perm_oc, None)
                break

    reg = [0, 0, 0, 0]
    for p in tests:
        reg = apply_opcode(p, reg, perm)
    yield reg[0]


def apply_opcode(
        instruction: list[int], reg: list[int], perm: list[int] | None = None
        ) -> list[int]:
    """
    Executes an opcode instruction on a register array using a permutation mapping.
    """
    if perm is None:
        perm = list(range(16))
    opcode, a, b, c = instruction

    match perm.index(opcode):
        case 0:
            reg[c] = reg[a] + reg[b]
        case 1:
            reg[c] = reg[a] + b
        case 2:
            reg[c] = reg[a] * reg[b]
        case 3:
            reg[c] = reg[a] * b
        case 4:
            reg[c] = reg[a] & reg[b]
        case 5:
            reg[c] = reg[a] & b
        case 6:
            reg[c] = reg[a] | reg[b]
        case 7:
            reg[c] = reg[a] | b
        case 8:
            reg[c] = reg[a]
        case 9:
            reg[c] = a
        case 10:
            reg[c] = a > reg[b]
        case 11:
            reg[c] = reg[a] > b
        case 12:
            reg[c] = reg[a] > reg[b]
        case 13:
            reg[c] = a == reg[b]
        case 14:
            reg[c] = reg[a] == b
        case 15:
            reg[c] = reg[a] == reg[b]
    return reg
