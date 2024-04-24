from dataclasses import dataclass
from collections import deque

@dataclass
class Beam:
    x: int
    y: int
    dx: int
    dy: int

def preprocessing(puzzle_input): 
    layout = {}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            layout[(x, y)] = c
    return layout, x + 1, y + 1

def solver(layout, w, h):
    yield energization(layout, w, h, 0, 0, 1, 0)
    max_left   = max(energization(layout, w, h, 0,     y,  1,  0)  for y in range(h))
    max_right  = max(energization(layout, w, h, w - 1, y,  -1, 0)  for y in range(h))
    max_top    = max(energization(layout, w, h, x,     0,  0,  1)  for x in range(w))
    max_bottom = max(energization(layout, w, h, h - 1, x,  0,  -1) for x in range(w))
    yield max(max_left, max_right, max_top, max_bottom)
                   

def energization(layout, w, h, x, y, dx, dy):
    beams = deque([Beam(x, y, dx, dy)])
    energized = set()
    while beams:
        beam = beams.popleft()
        while 0 <= beam.x < w and 0 <= beam.y < h:
            if (beam.x, beam.y, beam.dx, beam.dy) in energized: break
            else: energized.add((beam.x, beam.y, beam.dx, beam.dy))
            match layout[(beam.x, beam.y)], beam.dx, beam.dy:
                case '/', _, _: 
                    beam.dx, beam.dy = -beam.dy, -beam.dx
                case '\\', _, _ :
                    beam.dx, beam.dy = beam.dy, beam.dx
                case '|', _, 0 :
                    beam.dx = 0
                    beam.dy = 1
                    beams.append(Beam(beam.x, beam.y - 1, 0, -1))
                case '-', 0, _ :
                    beam.dx = 1
                    beam.dy = 0
                    beams.append(Beam(beam.x - 1, beam.y, -1, 0))
            beam.x += beam.dx
            beam.y += beam.dy
    return len(set((x, y) for (x, y, _, _) in energized))