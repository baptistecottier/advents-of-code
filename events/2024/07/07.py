from collections    import deque
from copy           import deepcopy
from operator       import add, mul


"""
Simply a parsing of the puzzle input with test value on one side and the 
available numbers on the other side
"""
def preprocessing(puzzle_input):
    equations = list()
    for line in puzzle_input.splitlines():
        test_value, numbers = line.split(': ')
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        equations.append((test_value, numbers))
    return equations


"""
Firstly compute the total calibratoion result considering only additions and
multiplicatins. Then recompute the total calibration result considering the 
concatenation operator.
"""
def solver(equations):
    yield get_calibration_result(deepcopy(equations), add, mul)
    yield get_calibration_result(equations, mul, add, concat_int)


"""
Given two integers a=(a_n...a_0) and b=(b_m...b_0), return a_n...a_0b_m...b_0
"""
def concat_int(a, b):
    return int(f"{a}{b}")


"""
For each pair of test_value and numbers, we compute all combinations possible 
of operators until one results in the test value. To avoid recomputing several 
times the same operation, we compute possibilities as a tree, where a branch is
cut if the calibration result is greater than the test value. 

Consider the following example : 136 : 81 40 15
            81              We start with the first value
           /  \                 
(40)      +    *            We compute the result for each available operation 
         /       \          (here, addition and multiplication)
        121      3240       As all numbers are positive and operations increase
       /   \                the result, we cut the branch with the value 3240 
(15)  +     *               but we keep going for the left branch and compute 
    /        \              the result for all operations. Here we can see than
  136        1815           using two additions leads to the test value.
"""
def get_calibration_result(equations, *available_operations):
    calibration_result = 0
    for test_value, numbers in equations:
        found = False
        equations = deque([numbers.pop(0)])
        while numbers:
            b = numbers.pop(0)
            next_equations = deque()
            while equations and not found:
                result = equations.pop()
                for f in available_operations:
                    temp = f(result, b)
                    if temp > test_value: 
                        continue
                    elif temp == test_value:
                        calibration_result += test_value
                        found = True
                        break
                    else: 
                        next_equations.append(temp)
            equations = next_equations
    return calibration_result
    