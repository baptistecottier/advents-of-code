from sympy import var, Eq
from sympy.solvers import solve
from pythonfw.functions import extract_chunks

def preprocessing(puzzle_input):
    """
    preprocessing extract chunks of 6 integers from puzzle_input.
    Each chunk then correspond to a machine.
    """
    return extract_chunks(puzzle_input, 6)


def solver(machines):
    """
    To solve, use the minimize_cost function. First without delta, then with the
    delta of 10_000_000_000_000 required for part 2.
    """
    yield minimize_cost(machines)
    yield minimize_cost(machines, 10_000_000_000_000)
    
    
def minimize_cost(machines, delta = 0):
    """
    Each machine is a system of two equations and two unknowns. We then solve
    systems and if both unknowns are integer, prize is reachable and tokens required
    are added to the total token cost. 
    """
    tokens = 0
    for xa, ya, xb, yb, xt, yt in machines:
        var('x y')
        eq1 = Eq(xa * x + xb * y, delta + xt)
        eq2 = Eq(ya * x + yb * y, delta + yt)
        solution = solve([eq1, eq2], dict = True)
        u, v = list(solution[0].values())
        if not (u % 1 or v % 1):
            tokens += 3 * u + v
    return int(tokens)