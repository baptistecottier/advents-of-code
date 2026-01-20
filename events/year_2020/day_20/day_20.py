"""
Advent of Code - Year 2020 - Day 20
https://adventofcode.com/2020/day/20
"""

from collections import defaultdict
from dataclasses import dataclass
from itertools import product
from math import prod


@dataclass
class Border:
    """
    Represents the borders of a tile with North, East, South, and West edges.
    """
    north: set
    east: set
    south: set
    west: set


@dataclass()
class Tile:
    """
    Represents a puzzle tile with an ID, borders, and body coordinates.
    """
    id: int
    borders: dict[tuple[int, int, int], Border]
    body: set[tuple[int, int]]


def assemble_jigsaw(tiles, image, matching_borders, size):
    """
    Assembles a jigsaw puzzle by processing each tile in the image grid and combining their body
    content. This function takes a grid of tile IDs and processes each tile by finding its correct
    orientation (rotation and/or flipping) based on matching borders. It then extracts the inner
    content of each tile (excluding the border pixels) and maps these coordinates to the final
    assembled image coordinate system. The function returns a set of coordinates representing all
    the active pixels in the assembled puzzle, where each tile's inner content is positioned
    according to its location in the grid.
    """
    final_coords = set()
    for y, line in enumerate(image):
        for x, tile_id in enumerate(line):
            tile = tiles[tile_id]
            bdy = tile.body
            r, v = get_orientation(tile, image, matching_borders, x, y)
            for _ in range(r):
                bdy = rotate(bdy, size)
            if v:
                bdy = flip(bdy, size)

            for tx, ty in product(range(0, (size - 2)), repeat=2):
                if (tx + 1, ty + 1) in bdy:
                    final_coords.add(((size - 2) * x + tx, (size - 2) * y + ty))
    return final_coords


def categorize_tiles(matching_borders):
    """
    Categorizes tiles based on their border matching patterns into corners, sides, and center
    pieces. This function analyzes a mapping of matching borders to determine the role of each tile
    in a puzzle grid. Tiles are classified as corners (matching value of 12), sides (matching value
    of 14), or others (center pieces) based on how many times their borders match with other tiles.
    Corner pieces have fewer matches since they're at grid edges, side pieces have moderate matches,
    and center pieces have the most matches.
    """
    matchs = defaultdict(int)
    for tiles_id in matching_borders.values():
        for tile_id in tiles_id:
            matchs[tile_id] += len(tiles_id)

    corners = set()
    sides = set()
    others = set()

    for k, v in matchs.items():
        if v == 12:
            corners.add(k)
        elif v == 14:
            sides.add(k)
        else:
            others.add(k)

    return (others, sides, corners)


def determine_tiles_position(tiles, categorized_tiles, matching_borders):
    """
    Determines the positions of puzzle tiles in a grid formation by placing them according to their
    matching borders. This function reconstructs a square image by positioning tiles based on their
    border relationships. It starts by placing a corner tile at position (0,0), then systematically
    fills the grid by finding tiles that share borders with already placed tiles. The function
    handles different types of tiles (corners, sides, others) and ensures proper adjacency by
    checking matching borders between neighboring positions.
    """
    img_side = int(len(tiles) ** .5)
    image = [[0 for _ in range(img_side)] for _ in range(img_side)]
    image[0][0] = categorized_tiles[2].pop()

    for j in range(img_side):
        for i in range(img_side):
            if j + i == 0:
                continue

            cddt_tiles = categorized_tiles[(j in [0, img_side - 1]) + (i in [0, img_side - 1])]

            found = False
            for tiles_id in matching_borders.values():
                if found:
                    break
                for tile in cddt_tiles:
                    if image[j - (j != 0)][i - (j == 0)] in tiles_id and tile in tiles_id:
                        image[j][i] = tile
                        cddt_tiles.remove(tile)
                        found = True
                        break
    return image


def flip(coords, size):
    """
    Flip coordinates vertically within a square of given size.
    """
    return {(size - 1 - x, y) for (x, y) in coords}


def get_borders(body, size):
    """
    Extract the border coordinates from a tile body and return a Border object.
    """
    borders = {(x, y) for (x, y) in body if x in [0, size - 1] or y in [0, size - 1]}
    north = {x for (x, y) in borders if y == 0}
    east = {y for (x, y) in borders if x == size - 1}
    south = {x for (x, y) in borders if y == size - 1}
    west = {y for (x, y) in borders if x == 0}
    return Border(north, east, south, west)


def get_orientation(tile, image, matching_borders, x, y):
    """
    Determines the valid orientations for a tile at a specific position in an image grid.
    This function analyzes the constraints imposed by neighboring tiles to find which
    orientations of the current tile would allow its borders to match with adjacent
    tiles.
    """
    img_side = len(image[0])
    v_direction = "south" if y < img_side - 1 else "north"
    h_direction = "east" if x < img_side - 1 else "west"

    goal = []
    orientations = set()
    for border, tiles_id in matching_borders.items():
        if tiles_id == {tile.id, image[y + 1 if y < img_side - 1 else y - 1][x]}:
            goal.append(set(border))

    for orientation, borders in tile.borders.items():
        if getattr(borders, v_direction) in goal:
            orientations.add(orientation)

    goal.clear()
    for border, tiles_id in matching_borders.items():
        if tiles_id == {tile.id, image[y][max((x + 1) % img_side, x-1)]}:
            goal.append(set(border))

    for orientation in orientations.copy():
        if all((getattr(tile.borders[orientation], h_direction) != g) for g in goal):
            orientations.remove(orientation)

    return orientations.pop()


def is_monster(x, y, coords):
    """
    Check if a sea monster pattern starts at coordinates (x, y) in the given coordinate set.
    """
    return all((pos in coords) for pos in (
        (x + 18, y),

        (x, y + 1), (x + 5, y + 1), (x + 6, y + 1), (x + 11, y + 1),
        (x + 12, y + 1), (x + 17, y + 1), (x + 18, y + 1), (x + 19, y + 1),

        (x + 1, y + 2), (x + 4, y + 2), (x + 7, y + 2),
        (x + 10, y + 2), (x + 13, y + 2), (x + 16, y + 2)
    ))


def rotate(coords, size):
    """
    Rotate coordinates 90 degrees clockwise within a square of given size.
    """
    return {(abs(size - y - 1), x) for (x, y) in coords}


def preprocessing(puzzle_input):
    """
    Parse the puzzle input and create Tile objects with borders and transformations.
    """
    list_tiles = [item.splitlines() for item in puzzle_input.split('\n\n')]
    size = len(list_tiles[0]) - 1
    tiles = {}

    for tile in list_tiles:
        tile_id = int(tile[0].split(' ')[1][:-1])
        body = {(x, y) for x, y in product(
                                    range(len(tile[1])),
                                    range(len(tile) - 1)) if tile[y + 1][x] == '#'}
        border = {}
        for r in range(4):
            border[(r, 0)] = get_borders(body, size)
            border[(r, 1)] = get_borders(flip(body, size), size)
            body = rotate(body, size)

        tiles[tile_id] = Tile(tile_id, border, body)

    return size, tiles


def solver(size, tiles):
    """
    Solve the puzzle by arranging tiles and finding sea monsters.
    """
    matching_borders = defaultdict(set)
    for tile, details in tiles.items():
        for b in details.borders.values():
            matching_borders[tuple(sorted(b.east))].add(tile)
            matching_borders[tuple(sorted(b.west))].add(tile)
            matching_borders[tuple(sorted(b.north))].add(tile)
            matching_borders[tuple(sorted(b.south))].add(tile)

    categorized_tiles = categorize_tiles(matching_borders)
    yield prod(categorized_tiles[2])

    image = determine_tiles_position(tiles, categorized_tiles, matching_borders)
    final_coords = assemble_jigsaw(tiles, image, matching_borders, size)

    pixel_width = int(len(tiles) ** .5) * (size - 2)
    n_sea_monsters = 0

    for orientation in range(8):
        if orientation % 2 == 1:
            final_coords = flip(final_coords, pixel_width)
        else:
            final_coords = rotate(final_coords, pixel_width)

        for x, y in product(range(pixel_width), repeat=2):
            if is_monster(x, y, final_coords):
                n_sea_monsters += 1

        if n_sea_monsters != 0:
            break

    yield len(final_coords) - 15 * n_sea_monsters
