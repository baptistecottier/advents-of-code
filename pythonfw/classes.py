from dataclasses import dataclass

@dataclass
class Direction:
    dx: int
    dy: int

class Register(dict):
    def __init__(self, *args):
        if len(args) == 1:
            super().__init__(*args)
        else: 
            super().__init__(zip('abcdefghixy', args + (11 - len(args)) * (0,)))
    def get(self, item):
        try :
            return self.__getitem__(item)
        except:
            return int(item)
        
class Point():
    def __init__(self, x = 0, y = 0, z = None) -> None:
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        if self.z: return f"x: {self.x}, y: {self.y}, z: {self.z}"
        else: return f"x: {self.x}, y: {self.y}"
    def manhattan(self, x = 0, y = 0, z = 0) -> int:
        if self.z: return abs(self.x - x) + abs(self.y - y) + abs(self.z - z)
        else: return abs(self.x - x) + abs(self.y - y)
    def xy(self):
        return (self.x, self.y)
    def xyz(self):
        return (self.x, self.y, self.z)
    def move(self, x = 0, y = 0, z = 0):
        self.x += x
        self.y += y
        if self.z != None : self.z += z
    def __lt__(self, other):
        return self.xy() < other.xy()

class Particule():
    def __init__(self, px, py, pz = 0, vx = 0, vy = 0, vz = 0, ax = 0, ay = 0, az = 0) -> None:
        self.p = Point(px, py, pz)
        self.v = Point(vx, vy, vz)
        self.a = Point(ax, ay, az)
    def pxy(self):
        return self.p.xy()
    def px(self):
        return self.p.x
    def py(self):
        return self.p.y
    def vx(self):
        return self.v.x
    def vy(self):
        return self.v.y
    def move(self):
        self.v.move(*self.a.xy())
        self.p.move(*self.v.xy())
    def __lt__(self, other):
        return (self.a.manhattan(), self.v.manhattan(), self.p.manhattan()) < (other.a.manhattan(), other.v.manhattan(), other.p.manhattan())
    def __repr__(self) -> str:
        return f"p=<{self.p.x},{self.p.y},{self.p.z}>, v=<{self.v.x},{self.v.y},{self.v.z}>, a=<{self.a.x},{self.a.y},{self.a.z}>"