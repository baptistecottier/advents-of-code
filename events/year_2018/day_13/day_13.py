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

    Args:
        circuit: Dictionary mapping (x,y) coordinates to track characters ('+', '\\', '/')
        carts: List of Cart objects with position, velocity, and choice state

    Returns:
        Tuple of (first_crash_location, last_cart_location) as strings

    Raises:
        ValueError: If no crash occurs during simulation

    Examples:
        >>> circuit = {(0,0): '+', (1,0): '-'}
        >>> carts = [Cart(0, 0, 1, 0), Cart(2, 0, -1, 0)]
        >>> solver(circuit, carts)
        ('1,0', '0,0')
    """
    tick = 0
    first_crash = None

    while len(carts) != 1:
        cart = carts.pop()
        cart.move()

        if cart.xy() in (item.xy() for item in carts):
            carts = list(item for item in carts if item.xy() != cart.xy())
            if first_crash is None:
                first_crash = str(cart)
            continue

        match (circuit[cart.xy()], abs(cart.vel.x)):
            case ('+', _):
                if cart.choice == 0:
                    cart.rotate_left()
                elif cart.choice == 2:
                    cart.rotate_right()
                cart.choice = (cart.choice + 1) % 3
            case ('\\', 0) | ('/', 1): cart.rotate_left()
            case ('\\', 1) | ('/', 0): cart.rotate_right()

        carts.insert(0, cart)
        if (tick := tick + 1) % len(carts) == 0:
            carts.sort(reverse=True, key=lambda x: x.pos)

    if first_crash is None:
        raise ValueError("No crash occurs!")

    return first_crash, str(carts[0])
