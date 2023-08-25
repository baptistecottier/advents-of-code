from typing import Generator
from pythonfw.functions     import screen_reader
from pythonfw.ship_computer import Program
from pythonfw.classes       import Point

class Robot(Point):
    def __init__(self, x: int =0, y: int = 0, z: int = None) -> None:
        super().__init__(x, y, z)
        self.dx: int = 0
        self.dy: int = -1
    def turn(self, b):
        if b: self.dx, self.dy = - self.dy, self.dx
        else: self.dx, self.dy = self.dy, -self.dx
        self.move(self.dx, self.dy)

        
def preprocessing(input: str) -> list[int]: 
    return list(map(int, input.split(',')))


def solver(intcode: list[int]) -> Generator:
    _, whited = paint(intcode, set())
    yield len(whited)

    white, _ = paint(intcode, {(0, 0)})
    yield screen_reader(white)


def paint(intcode: list[int], white: set) -> tuple[set]:
    whited: set      = set()
    position: Robot  = Robot()
    painter: Program = Program(intcode)
    
    while not painter.halt:
        color = int(position.xy() in white)
        match painter.run(color), color:
            case 1, 0: 
                white.add(position.xy())
                whited.add(position.xy())
            case 0, 1: 
                white.remove(position.xy())
        position.turn(painter.run(color))
    return white, whited