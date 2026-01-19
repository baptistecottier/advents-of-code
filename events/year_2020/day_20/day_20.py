# pylint: skip-file
# flake8: noqa
# type: ignore
"""
Advent of Code - Year 2020 - Day 20
https://adventofcode.com/2020/day/20
"""

from itertools import product
from math      import prod
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Border:
    N: set
    E: set
    S: set
    W: set

@dataclass(unsafe_hash=True)
class Tile:
    id: int
    borders: Border
    body: dict
    score: dict 
    rotate: int = 0
    flip: int = 0

def get_borders(body, size):
    borders = {(x, y) for (x, y) in body if x in [0, size - 1] or y in [0, size - 1]}
    north = {x for (x, y) in borders if y == 0}
    east = {y for (x, y) in borders if x == size - 1}
    south = {x for (x, y) in borders if y == size - 1}
    west = {y for (x, y) in borders if x == 0}
    return Border(north, east, south, west)

def preprocessing(puzzle_input):
    list_tiles = [item.splitlines() for item in puzzle_input.split('\n\n')]
    size = len(list_tiles[0]) - 1
    score = {(a, b, c): set() for a, b, c in product((0, 1, 2, 3), (0, 1), (0, 1))}
    tiles = []

    for tile in list_tiles:
        tile_id = int(tile[0].split(' ')[1][:-1])
        body = {(x, y) for x, y in product(
                                    range(len(tile[1])),
                                    range(len(tile) - 1)) if tile[y + 1][x] == '#'}

        border = {(0, 0, 0): get_borders(body, size),
                  (0, 1, 0): get_borders(flipv(body, size), size),
                  (0, 0, 1): get_borders(fliph(body, size), size),
                  (0, 1, 1): get_borders(flipv(fliph(body, size), size), size)
                  }

        for r in [1]:
            _body = rotate(body, size)
            # if r == 3:
            #     body = rotate(body, size)

            border[(r, 0, 0)] = get_borders(_body, size)
            border[(r, 1, 0)] = get_borders(flipv(_body, size), size)
            border[(r, 0, 1)] = get_borders(fliph(_body, size), size)

        tiles.append(Tile(tile_id, border, body, score))

    return size, tiles

def rotate(coords, size):
    return {(abs(size - y - 1), x) for (x, y) in coords}  

def flipv(coords, size):
    return {(size - 1 - x, y) for (x, y) in coords}  

def fliph(coords, size):
    return {(x, size - 1 - y) for (x, y) in coords}  

def display(coords, size):
    for y in range(size):
        line = ""
        for x in range(size):
            if (x, y) in coords : line+='#'
            else : line += '.'
        print(line)

def is_monster(x, y, coords):
    return all((pos in coords) for pos in (
        (x + 18, y),
        (x, y + 1), (x+ 5, y + 1), (x + 6, y + 1), (x + 11, y + 1), (x + 12, y + 1), (x+ 17, y + 1), (x + 18, y + 1), (x + 19, y + 1),
        (x + 1, y + 2), (x + 4, y + 2), (x + 7, y + 2), (x + 10, y + 2), (x + 13, y + 2), (x + 16, y + 2)
    ))

def solver(size, tiles: Tile):
    t = defaultdict(set)
    for tile in tiles:
        border = tile.borders
        for b in border.values():
            t[tuple(sorted(b.E))].add(tile.id)
            t[tuple(sorted(b.W))].add(tile.id)
            t[tuple(sorted(b.N))].add(tile.id)
            t[tuple(sorted(b.S))].add(tile.id)
    matchs = defaultdict(int)
    for v in t.values():
        for vv in v:
            matchs[vv]+= len(v)
    corners = set()
    y = t.values()
    sides = set()
    others = set()
    img_side = int(len(tiles) ** .5)


    image = [[0 for _ in range(img_side)] for _ in range(img_side)]
    for k, v in matchs.items():
        if v == 12:
            corners.add(k)
        elif v == 14:
            sides.add(k)
        else:
            others.add(k)

    yield prod(corners)
    current = corners.pop()

    image[0][0] = current

    i = 1
    while i < img_side - 1:
        found = False
        for a in y:
            if found:
                break
            if current in a:
                for s in sides:
                    if s in a:
                        sides.remove(s)
                        current = s
                        image[0][i] = current
                        i += 1
                        found = True
                        break
    found = False
    for a in y:
            if found:
                break
            if current in a:
                for s in corners:
                    if s in a:
                        corners.remove(s)
                        current = s
                        image[0][i] = current
                        i += 1
                        found = True
                        break

    for j in range(1, img_side - 1):
        found = False
        for a in y:
            if found:
                break
            if image[j-1][0] in a:
                for s in sides:
                    if s in a:
                        image[j][0] = s
                        sides.remove(s)
                        found = True
                        break
        found = False
        for a in y:
            if found:
                break
            if image[j-1][img_side - 1] in a:
                for s in sides:
                    if s in a:
                        image[j][img_side - 1] = s
                        sides.remove(s)
                        found = True
                        break
        
        for i in range(1, img_side - 1):
            found = False
            for a in y:
                if found:
                    break
                if image[j][i-1] in a:
                    for o in others:
                        if o in a:
                            if {image[j-1][i], o} not in y:
                                continue
                            found = True
                            image[j][i] = o
                            others.remove(o)
                            break
    found = False
    for a in y:
        if found:
            break
        if image[img_side - 2][0] in a:
            for s in corners:
                if s in a:
                    image[img_side - 1][0] = s
                    corners.remove(s)
                    found = True
                    break
    found = False
    for a in y:
        if found:
            break
        if image[img_side - 2][img_side - 1] in a:
            for s in corners:
                if s in a:
                    image[img_side - 1][img_side - 1] = s
                    corners.remove(s)
                    found = True
                    break
    
    for i in range(1, img_side - 1):
        found = False
        for a in y:
            if found:
                break
            if image[img_side - 1][i-1] in a:
                for o in sides:
                    if o in a:
                        if {image[img_side - 2][i], o} not in y:
                            continue
                        found = True
                        image[img_side - 1][i] = o
                        sides.remove(o)
                        break

    candidates = {}

    for y, line in enumerate(image):
        for x, tile in enumerate(line):
            candidates[tile] = set()
            goal = []
            if y < img_side - 1:
                for k, _v in t.items():
                    if _v == {image[y][x], image[y+1][x]}:
                        goal.append(set(k))

        
                for tt in tiles: # type: ignore
                    if tt.id == image[y][x]:
                        for (rr, vv, hh), v in tt.borders.items():
                            if getattr(v, "S") in goal:
                                candidates[tt.id].add((rr, vv, hh))
                goal = []
                for k, _v in t.items():
                    if x < img_side - 1:
                        if _v == {image[y][x], image[y][x+1]}:
                            goal.append(set(k))
                    if x == img_side - 1:
                        if _v == {image[y][x-1], image[y][x]}:
                            goal.append(set(k))


                for (rr, vv, hh) in candidates[image[y][x]].copy():
                    for ttt in tiles:
                        if ttt.id == image[y][x]:
                            if x < img_side - 1:
                                if all((ttt.borders[(rr, vv, hh)].E != g) for g in goal):
                                    candidates[ttt.id].remove((rr, vv, hh))

                            if x == img_side - 1:
                                if all((ttt.borders[(rr, vv, hh)].W != g) for g in goal):
                                    candidates[ttt.id].remove((rr, vv, hh))
                                break
            if y == img_side - 1:
                for k, _v in t.items():
                    if _v == {image[y-1][x], image[y][x]}:
                        goal.append(set(k))
        
                for tt in tiles:
                    if tt.id == image[y][x]:
                        for (rr, vv, hh), v in tt.borders.items():
                            if getattr(v, "N") in goal:
                                candidates[tt.id].add((rr, vv, hh))

                goal = []
                for k, _v in t.items():
                    if x < img_side - 1:
                        if _v == {image[y][x], image[y][x+1]}:
                            goal.append(set(k))
                    if x == img_side - 1:
                        if _v == {image[y][x-1], image[y][x]}:
                            goal.append(set(k))

                for (rr, vv, hh) in candidates[image[y][x]].copy():
                    for ttt in tiles:
                        if ttt.id == image[y][x]:
                            if x < img_side - 1:
                                if all((ttt.borders[(rr, vv, hh)].E != g) for g in goal):
                                    candidates[ttt.id].remove((rr, vv, hh))

                            if x == img_side - 1:
                                if all((ttt.borders[(rr, vv, hh)].W != g) for g in goal):
                                    candidates[ttt.id].remove((rr, vv, hh))
                                break

    final_coords = set()
    final = [['.' for _ in range(img_side * (size - 2))] for _ in range(img_side * (size - 2))]
    for y, line in enumerate(image):
        for x, tile in enumerate(line):
            for _t in tiles:
                if _t.id == tile:
                    bdy = _t.body
                    r, v, h = candidates[tile].pop()

                    for _ in range(r):
                        bdy = rotate(bdy, size)
                    if v:
                        bdy = flipv(bdy, size)
                    if h:
                        bdy = fliph(bdy, size)
                    for tx in range(0, (size - 2)):
                        for ty in range(0, (size - 2)):
                            if (tx + 1, ty + 1) in bdy:
                                final[(size - 2)*y + ty][(size - 2)*x + tx] = '#'
                                final_coords.add(((size - 2)*x + tx, (size - 2)*y + ty))
                    break

                    

    for r in range(4):
        for v in range(2):
            for h in range(2):
                cnt = 0
                coords = final_coords.copy()
                for _ in range(r):
                    coords = rotate(coords, img_side * (size - 2))
                if v:
                    coords = flipv(coords, img_side * (size - 2))
                if h:
                    coords = fliph(coords, img_side * (size - 2))
                for x in range(img_side * (size - 2)):
                    for y in range(img_side * (size - 2)):
                            if is_monster(x, y, coords):
                                cnt += 15
                if cnt != 0:
                    yield len(final_coords) - cnt
                    return