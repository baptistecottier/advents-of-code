"""
Advent of Code - Year 2018 - Day 13
https://adventofcode.com/2018/day/13
"""

from pythonfw.classes import Particule2D


class Cart(Particule2D):
    """
    A cart that moves on a 2D grid, inheriting from Particule2D with position and direction
    tracking.
    """
    def __init__(self, x, y, dx, dy) -> None:
        super().__init__((x, y), (dx, dy))
        self.choice = 0


def preprocessing(puzzle_input: str) -> tuple[dict[tuple[int, int], str], list[Cart]]:
    """
    Parse puzzle input to extract circuit layout and initialize cart positions.
    """
    circuit = {}
    carts = []
    dx = {'>': 1, '<': -1}
    dy = {'v': 1, '^': -1}

    for y, row in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(row):
            circuit[(x, y)] = c
            if c in '><v^':
                carts.insert(0, Cart(x, y, dx.get(c, 0), dy.get(c, 0)))

    return (circuit, carts)


def solver(circuit: dict[tuple[int, int], str], carts: list[Cart]) -> tuple[str, str]:
    """
    Simulates cart movement on a circuit until only one cart remains.
    """
    first_crash = ""
    new_carts = []

    while True:
        cart = carts.pop()
        cart.move()
        crash = False
        for _carts in [carts, new_carts]:
            for c in _carts:
                if cart.xy() == c.xy():
                    if first_crash == "":
                        first_crash = str(cart)
                    _carts.remove(c)
                    crash = True

        if not crash:
            match (circuit[cart.xy()], abs(cart.vel.x), cart.choice):
                case ('\\', 0, _) | ('/', 1, _) | ('+', _, 0): cart.rotate_left()
                case ('\\', 1, _) | ('/', 0, _) | ('+', _, 2): cart.rotate_right()
            if circuit[cart.xy()] == '+':
                cart.choice = (cart.choice + 1) % 3
            new_carts.append(cart)

        if carts == []:
            if len(new_carts) == 1:
                last_cart = new_carts.pop()
                return first_crash, last_cart
            carts = sorted(new_carts, reverse=True, key=lambda x: x.pos)
            new_carts.clear()
