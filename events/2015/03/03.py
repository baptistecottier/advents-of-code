from copy import deepcopy
from dataclasses import dataclass

@dataclass
class Direction:
    dx: int
    dy: int

@dataclass(unsafe_hash=True)
class Position:
    x: int
    y: int
    def move(self, d: Direction):
        return Position(self.x + d.dx, self.y + d.dy)
    
def preprocessing(puzzle_input):
    converter  = {'^': Direction(0, 1), '>': Direction(1, 0), 'v': Direction(0, -1), '<': Direction(-1, 0)}
    directions = list(converter.get(d) for d in puzzle_input)
    return directions


def solver(directions_):
    
    def deliver(n):
        directions = deepcopy(directions_)
        deliverers = [Position(0, 0) for _ in range(n)]
        houses     = {Position(0, 0)}
        
        while directions:
            for k in range(n):
                d = directions.pop(0)
                p = deliverers.pop(0)
                p = p.move(d)
                houses.add(p)
                deliverers.append(p)
        return len(houses)
    
    yield deliver(1)
    yield deliver(2)