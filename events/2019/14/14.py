# from sympy.solvers import solve
# from sympy import var, Eq

# def preprocessing(puzzle_input):
#     reactions = dict()
#     for reaction in puzzle_input.splitlines():
#         before, after = reaction.split(" => ")
#         after_qty, after_name = after.split()
#         reactions[after_name] = {"CREATED": int(after_qty)}
#         for chemical in before.split(", "):
#             qty, name = chemical.split()
#             reactions[after_name][name] = int(qty)
#     return reactions

# def solver(reactions):
#     required = {k :v for k, v in reactions["FUEL"].items() if k != "CREATED"}
#     print(required)
#     while required.keys() != set(["ORE"]):
#         updated_required = {"ORE": 0}
#         for k, v in required.items():
#             if k == "ORE":
#                 updated_required["ORE"] += v
#             else:
                
#     yield 1
import numpy as np

def preprocessing(puzzle_input):
    return puzzle_input

def solver(puzzle_input):
    # a = np.array([[-10, 0, 0, 0, 0, 0, 10],[0, -1, 0, 0, 0, 0, 1], [7, 1, -1, 0, 0, 0, 0], \
    #                 [7,0, 1, -1, 0, 0, 0], [7,0, 0, 1, -1, 0, 0], [7,0, 0, 0, 1, -1, 0]])
    # b = np.array([0, 0, 0, 0, 0, 0])
    a = np.array([[-2,    0,      0,      0,      0,      0,      0,      9],\
                    [0,     -3,     0,      0,      0,      0,      0,      8],\
                    [0,     0,      -5,     0,      0,      0,      0,      7],\
                    [3,     4,      0,      -1,     0,      0,      0,      0],\
                    [0,     5,      7,      0,      1,      0,      0,      0],\
                    [1,     0,      4,      0,      0,      -1,     0,      0],\
                    [0,     0,      0,      2,      3,      4,      -1,     0]])
    b = np.array([0, 0, 0, 0, 0, 0, 0])
    print(np.linalg.lstsq(a, b))
    yield 2
"""
A       B       C       D       E   FUEL    ORE
-10     0       0       0       0   0       -10
0       -1                                  1
7       1       -1                              
7               1       -1
7                       1       -1
1                               1   -1
"""

"""
A       B       C       AB      BC      CA   FUEL    ORE
[-2,    0,      0,      0,      0,      0,      0,      9],\
[0,     -3,     0,      0,      0,      0,      0,      8],\
[0,     0,      -5,     0,      0,      0,      0,      7],\
[3,     4,      0,      -1,     0,      0,      0,      0],\
[0,     5,      7,      0,      1,      0,      0,      0],\
[1,     0,      4,      0,      0,      -1,     0,      0],\
[0,     0,      0,      2,      3,      4,      -1,     0]
"""