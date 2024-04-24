from string import ascii_uppercase
from re     import findall
from copy   import deepcopy

def preprocessing(puzzle_input):
    instructions = {c: set() for c in ascii_uppercase}
    steps = findall(r'[A-Z]', puzzle_input)
    while steps:
        instructions[steps.pop()].add(steps.pop())
        steps.pop()
    return instructions

def solver(requirements):
    yield part_1(deepcopy(requirements))
    yield part_2(requirements)
    
def part_1(requiremenents):
    started  = list(ascii_uppercase)
    finished = list()
    
    while len(finished) != 26:
        for step in started: 
            if requiremenents[step] <= set(finished): 
                finished.append(step)
                started.remove(step)
                del requiremenents[step]
                break
    return ''.join(finished)
        
def part_2(requiremenents):
    started  = list()
    finished = set()
    waiting  = list(ascii_uppercase)
    workers  = [[str(), 0] for _ in range(5)]
    second   = 0
    
    for step in ascii_uppercase: 
        if requiremenents[step] <= finished:
            started.append(step)
        
    while len(finished) != 26:
        for worker_step, countdown in workers:
            if countdown == 0 and worker_step: 
                finished.add(worker_step)
                for step in waiting: 
                    if requiremenents[step] <= finished: 
                        started.append(step)
                        
        for i, worker in enumerate(workers):    
            if worker[1] <= 0:
                if started: 
                    x = started.pop(0)
                    waiting.remove(x)
                    workers[i] = [x, ord(x) - 5]
            worker[1] -= 1
        second += 1
    return second - 1