from aoctools.classes import Particule

class Cart(Particule):
    def __init__(self, x, y, dx, dy) -> None:
        super().__init__(x, y, 0, dx, dy, 0)
        self.choice = 0
        pass
    
    def turn_right(self):
        match self.v.xy():
            case (n, 0): 
                self.v.x = 0
                self.v.y = n
            case (0, n): 
                self.v.x = -n
                self.v.y = 0
                
    def turn_left(self):
        match self.v.xy():
            case (n, 0): 
                self.v.x = 0
                self.v.y = -n
            case (0, n): 
                self.v.x = n
                self.v.y = 0
          
      
def preprocessing(input):
    circuit = dict()
    carts = []
    dx = {'>': 1, '<': -1}
    dy = {'v': 1, '^': -1}
    for y, row in enumerate(input.splitlines()):
        for x, c in enumerate(row):
            circuit[(x, y)] = c
            if c in '><v^': 
                carts.insert(0, Cart(x, y, dx.get(c, 0), dy.get(c, 0)))
    return (circuit, carts)

def solver(race): 
    circuit, carts = race
    tick = 0
    first_crash = True
    while len(carts) != 1: 
        cart = carts.pop()
        cart.move()
        if cart.pxy() in (item.pxy() for item in carts): 
            carts = list(item for item in carts if item.pxy() != cart.pxy())
            if first_crash: yield f"{cart.p.x},{cart.p.y}"
            first_crash = False
            continue
        
        match (circuit[cart.pxy()], abs(cart.vx())):
            case ('+', _):  
                if cart.choice == 0: cart.turn_left()
                elif cart.choice == 2: cart.turn_right()
                cart.choice = (cart.choice + 1) % 3
            case ('\\', 0) | ('/', 1): cart.turn_left()
            case ('\\', 1) | ('/', 0): cart.turn_right()
        carts.insert(0, cart)
                
        if (tick:= tick + 1) % len(carts) == 0: 
            carts.sort(reverse = True, key = lambda x : x.p)
    yield f"{carts[0].px()},{carts[0].py()}"