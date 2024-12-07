def preprocessing(puzzle_input):
    tests = list()
    for line in puzzle_input.splitlines():
        goal, numbers = line.split(': ')
        goal = int(goal)
        numbers = list(map(int, numbers.split()))
        tests.append((goal, numbers))
    return tests

import operator
import itertools
from copy import deepcopy
def solver(tests):
    cnt_wo_concat = 0
    cnt_w_concat = 0
    for goal, numbers in tests:
        found = False
        for op in itertools.product((operator.add, operator.mul, cont), repeat=len(numbers)- 1):
            concat = False
            if cont in op : concat = True
            if found: break
            co_numbers = deepcopy(numbers)
            score = co_numbers.pop(0)
            ops = list(op)
            while ops:
                o = ops.pop(0)
                b = co_numbers.pop(0)
                score = o(score, b)
                if score > goal: 
                    break
                if score == goal: 
                    if concat:
                        cnt_w_concat += goal
                    else: 
                        cnt_wo_concat += goal
                    found = True
                    break
                       
                       
    yield cnt_wo_concat
    yield cnt_w_concat + cnt_wo_concat
    
def cont(a, b):
    return int(f"{a}{b}")