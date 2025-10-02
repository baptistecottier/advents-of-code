aoc::main!();

fn preprocessing(puzzle_input: &str) -> Vec<Vec<(i32, i32)>> {
    puzzle_input
        .lines()
        .enumerate()
        .map(|(y, line)| {
            line.char_indices()
                .filter(|&(_, c)| c != '.')
                .map(|(x, c)| (c, (x as i32, y as i32)))
                .collect_vec()
        })
        .flatten()
        .into_group_map()
        .into_iter()
        .map(|v| v.1)
        .collect_vec()
}

fn part_1(antennas: Vec<Vec<(i32, i32)>>) -> usize {
    n_locations(antennas, 1..2)
}

fn part_2(antennas: Vec<Vec<(i32, i32)>>) -> usize {
    n_locations(antennas, 0..50)
}

fn n_locations(antennas: Vec<Vec<(i32, i32)>>, range: Range<i32>) -> usize {
    antennas
        .iter()
        .map(|antenna| {
            antenna
                .iter()
                .combinations(2)
                .map(|v| (v[0], v[1]))
                .map(|((xa, ya), (xb, yb))| {
                    range
                        .clone()
                        .map(|delta| {
                            [
                                (delta * (xa - xb) + xa, delta * (ya - yb) + ya),
                                (delta * (xb - xa) + xb, delta * (yb - ya) + yb),
                            ]
                        })
                        .flatten()
                        .into_iter()
                        .collect::<Vec<(i32, i32)>>()
                })
                .flatten()
        })
        .flatten()
        .unique()
        .filter(|(x, y)| (0..50).contains(x) && (0..50).contains(y))
        .count()
}
