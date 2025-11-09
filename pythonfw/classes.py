"""
Some tool-classes repeatedly used in advent of code
"""


class Register(dict):
    """
    A dictionary-based register that maps letter keys to integer values and can retrieve values
    from either literals or registry lookups.
    """
    def __init__(self, *args):
        if len(args) == 1:
            super().__init__(*args)
        else:
            super().__init__(zip('abcdefghixy', args + (11 - len(args)) * (0,)))

    def get_value(self, item):
        """
        Returns integer value: literal if digit string, otherwise registry lookup.
        """
        if item.lstrip('+-').isdigit():
            return int(item)
        return self[item]


class Point():
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        if self.z:
            return f"x: {self.x}, y: {self.y}, z: {self.z}"
        return f"x: {self.x}, y: {self.y}"

    def manhattan(self, x=0, y=0, z=0) -> int:
        if self.z:
            return abs(self.x - x) + abs(self.y - y) + abs(self.z - z)
        return abs(self.x - x) + abs(self.y - y)

    def xy(self):
        return (self.x, self.y)

    def xyz(self):
        return (self.x, self.y, self.z)

    def move(self, x=0, y=0, z=0):
        self.x += x
        self.y += y
        self.z += z

    def __lt__(self, other):
        return self.xy() < other.xy()


class Particule():
    def __init__(self, px, py, pz=0, vx=0, vy=0, vz=0, ax=0, ay=0, az=0) -> None:
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
        self_dist = (self.a.manhattan(), self.v.manhattan(), self.p.manhattan())
        other_dist = (other.a.manhattan(), other.v.manhattan(), other.p.manhattan())
        return self_dist < other_dist

    def __repr__(self) -> str:
        return f"""
p=<{self.p.x},{self.p.y},{self.p.z}>,
v=<{self.v.x},{self.v.y},{self.v.z}>,
a=<{self.a.x},{self.a.y},{self.a.z}>"""


class Particule2D():
    """A 2D particle with position, velocity, and acceleration that can be rotated and reversed."""
    def __init__(
            self,
            p: tuple[int, int] = (0, 0),
            v: tuple[int, int] = (0, 0),
            a: tuple[int, int] = (0, 0)
            ) -> None:
        self.pos = Point(*p)
        self.vel = Point(*v)
        self.acc = Point(*a)

    def __str__(self):
        return f"{self.pos.x},{self.pos.y}"

    def rotate_right(self):
        """Rotates the current velocity vector 90 degrees counter-clockwise."""
        self.vel.x, self.vel.y = - self.vel.y, self.vel.x

    def rotate_left(self):
        """Rotates the velocity vector 90 degrees clockwise."""
        self.vel.x, self.vel.y = self.vel.y, - self.vel.x

    def reverse(self):
        """Reverses the velocity vector by negating both x and y components."""
        self.vel.x, self.vel.y = - self.vel.x, - self.vel.y

    def xy(self):
        """Returns the x and y coordinates as a tuple."""
        return (self.pos.x, self.pos.y)

    def move(self):
        """Updates position by applying acceleration to velocity and velocity to position."""
        self.vel.x += self.acc.x
        self.vel.y += self.acc.y
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
