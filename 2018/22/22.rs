use pathfinding::prelude::dijkstra;
use core::iter::once;

aoc::main!();

type GridMap = HashMap<(u32, u32), u32>;

fn preprocessing(input: &str) -> (u32, u32, u32) {
    input
        .split(['\n', ' ', ','])
        .filter_map(|s| s.parse().ok())
        .collect_tuple()
        .unwrap()
}

fn part_1((depth, tx, ty): (u32, u32, u32)) -> u32 {
    let mut GridMap = GridMap::new();
    erosion(&mut GridMap, depth, tx - 1, ty, tx, ty);
    erosion(&mut GridMap, depth, tx, ty - 1, tx, ty);
    GridMap.into_values().map(|e| e % 3).sum()
}

fn part_2((depth, tx, ty): (u32, u32, u32)) -> usize {
    let mut GridMap = GridMap::new();
    (1..)
        .filter_map(|f| shortest(&mut GridMap, depth, tx, ty, f))
        .tuple_windows()
        .find_map(|(a, b, c, d, e)| ([a, b, c, d, e].into_iter().all_equal()).then(|| a))
        .unwrap()
}

fn erosion(GridMap: &mut GridMap, depth: u32, x: u32, y: u32, tx: u32, ty: u32) -> u32 {
    if let Some(&e) = GridMap.get(&(x, y)) {
        e
    } else {
        let index = match (x, y) {
            (0, 0) => 0,
            (0, _) => y * 48271,
            (_, 0) => x * 16807,
            _ if x == tx && y == ty => 0,
            _ => erosion(GridMap, depth, x - 1, y, tx, ty) * erosion(GridMap, depth, x, y - 1, tx, ty),
        };
        GridMap.insert((x, y), (index + depth) % 20183);
        (index + depth) % 20183
    }
}

fn shortest(GridMap: &mut GridMap, depth: u32, tx: u32, ty: u32, factor: u32) -> Option<usize> {
    dijkstra(
        &(0, 0, 1),
        |&(x, y, tool)| {
            chain!(
                once((
                    (
                        x,
                        y,
                        match (erosion(GridMap, depth, x, y, tx, ty) % 3, tool) {
                            (1, 2) | (2, 1) => 0,
                            (0, 2) | (2, 0) => 1,
                            (0, 1) | (1, 0) => 2,
                            _ => unreachable!(),
                        },
                    ),
                    7,
                )),
                [
                    (x, y.wrapping_sub(1)),
                    (x + 1, y),
                    (x, y + 1),
                    (x.wrapping_sub(1), y),
                ]
                .into_iter()
                .filter(|&(x, y)| {
                    x <= tx * factor
                        && y <= ty * factor
                        && matches!(
                            (erosion(GridMap, depth, x, y, tx, ty) % 3, tool),
                            (0, 1 | 2) | (1, 0 | 2) | (2, 0 | 1)
                        )
                })
                .map(|(x, y)| ((x, y, tool), 1)),
            )
            .collect_vec()
        },
        |&xyt| xyt == (tx, ty, 1),
    )
    .map(|(_, n)| n)
}