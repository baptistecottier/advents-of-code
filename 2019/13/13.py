from pythonfw.ship_computer  import Program
from pythonfw.classes        import Point
from pythonfw.functions      import sign

def preprocessing(input_: str) -> list[int]:
    return list(map(int, input_.split(',')))

def solver(intcode: list[int]):
    block: int      = 0    
    arcade: Program = Program(intcode)
    while not arcade.halt:
        _, _, id = (arcade.run() for _ in range(3))
        if id == 2: block += 1
    yield block
    
    ball: int       = 0
    score: int      = 0
    paddle: int     = 0
    arcade: Program = Program([2] + intcode[1:])
    
    while not arcade.halt:
        input_ = sign(ball - paddle)
        x, _, id  = (arcade.run(input_) for _ in range(3))
        match (x, id):
            case (-1, _): score  = id
            case (_, 3):  paddle = x
            case (_, 4):  ball   = x
    yield score