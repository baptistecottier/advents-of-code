"""Advent of Code - Year 2017 - Day 18"""

from pythonfw.classes import Register

def preprocessing(puzzle_input: str) -> list[list[str]]:
    """
    Parse the puzzle input into a list of lists, splitting each line by space.
    """
    return [line.split(' ') for line in puzzle_input.splitlines()]


def solver(instructions: list[list[str]]):
    """
    Solves both parts of the puzzle: finding recovered frequency and counting sent values.
    """
    yield (1, get_frequency_when_recovered(instructions))
    yield (2, count_sent_values(instructions))


def get_frequency_when_recovered(instructions: list[list[str]]) -> int:
    """
    Process a list of instructions and return the last played sound frequency when recovered.
    
    The function executes instructions in sequence which can modify registers, play sounds,
    and recover the last played sound frequency. Execution stops when a 'rcv' instruction
    is encountered.
    
    Instructions include:
    - 'snd X': plays a sound with frequency equal to the value of X
    - 'set X Y': sets register X to the value of Y
    - 'add X Y': increases register X by the value of Y
    - 'mul X Y': multiplies register X by the value of Y
    - 'mod X Y': sets register X to X modulo Y
    - 'rcv X': recovers the last sound played if X > 0
    - 'jgz X Y': jumps with an offset of Y if X > 0
    
    Args:
        instructions: A list of instructions, where each instruction is a list of strings.
                     The first element is the operation, followed by operands.
    
    Returns:
        The value of the last played sound frequency when a recovery instruction is reached.
    """
    reg = Register({'a': 0,'b': 0,'f': 0,'i': 0,'p': 0})
    d = instructions[0]
    i = 0
    sound_frequency = 0
    while instructions[i][0] != 'rcv':
        d = instructions[i]
        match d[0]:
            case 'snd': sound_frequency = reg.get(d[1])
            case 'set': reg[d[1]] = reg.get(d[2])
            case 'add': reg[d[1]] += reg.get(d[2])
            case 'mul': reg[d[1]] *= reg.get(d[2])
            case 'mod': reg[d[1]] %= reg.get(d[2])
            case 'rcv':
                if reg[d[1]] > 0:
                    reg[d[1]] = sound_frequency
            case 'jgz':
                if reg.get(d[1]) != 0:
                    i += int(d[2]) - 1
        i += 1
    return sound_frequency

def count_sent_values(instructions: list[list[str]]) -> int:
    """
    Count the number of values sent by program 1 during concurrent execution of two programs.
    
    The function simulates two programs running in parallel, each with its own set of registers,
    processing instructions and communicating via queues. Each program has its 'p' register
    initialized to its program ID (0 or 1).
    
    Instructions include:
    - 'snd X': sends the value of X to the other program's queue
    - 'set X Y': sets register X to the value of Y
    - 'add X Y': increases register X by the value of Y
    - 'mul X Y': multiplies register X by the value of Y
    - 'mod X Y': sets register X to X modulo Y
    - 'rcv X': receives a value for register X, or switches programs if queue is empty
    - 'jgz X Y': jumps with an offset of Y if X > 0
    
    Args:
        instructions: A list of instructions, where each instruction is a list of strings.
                     The first element is the operation, followed by operands.
    
    Returns:
        The number of values sent by program 1.
    """
    reg = [Register({'a': 0,'b': 0,'f': 0,'i': 0,'p': 0}),
           Register({'a': 0,'b': 0,'f': 0,'i': 0,'p': 1})]
    queue =[[], []]
    p = 1
    i = [0,0]
    cnt = 0
    while 1:
        d = instructions[i[p]]
        match d[0]:
            case 'snd':
                cnt += p
                queue[1-p].insert(0, reg[p].get(d[1]))
            case 'set': reg[p][d[1]]  = reg[p].get(d[2])
            case 'add': reg[p][d[1]] += reg[p].get(d[2])
            case 'mul': reg[p][d[1]] *= reg[p].get(d[2])
            case 'mod': reg[p][d[1]] %= reg[p].get(d[2])
            case 'rcv':
                if 0 not in i and queue == [[],[]]:
                    break
                if not queue[p]:
                    p = 1 - p
                    i[p] -= 1
                else: reg[p][d[1]] = queue[p].pop()
            case 'jgz':
                if reg[p].get(d[1]) > 0:
                    i[p] += reg[p].get(d[2]) - 1
        i[p] += 1
    return cnt
