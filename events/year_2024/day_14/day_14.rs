aoc::main!();

fn preprocessing(puzzle_input: &str) -> Vec<(i32, i32, i32, i32)> {
    puzzle_input
        .replace("p=", "")
        .replace("v=", "")
        .lines()
        .map(|robot| {
            robot
                .split(&[' ', ','])
                .map(|n| n.parse().unwrap())
                .collect_tuple()
                .unwrap()
        })
        .collect_vec()
}

fn part_1(robots: Vec<(i32, i32, i32, i32)>) -> usize {
    robots
        .iter()
        .map(|(px, py, vx, vy)| {
            (
                (px + 100 * vx).rem_euclid(101),
                (py + 100 * vy).rem_euclid(103),
            )
        })
        .filter(|(x, y)| (*x != 50) && (*y != 51))
        .map(|(x, y)| (x / 51, y / 52))
        .counts()
        .values()
        .product()
}

fn part_2(robots: Vec<(i32, i32, i32, i32)>) -> i32 {
    (1..)
        .map(|seconds| {
            (
                seconds,
                robots
                    .iter()
                    .map(move |(px, py, vx, vy)| {
                        (
                            (px + seconds * vx).rem_euclid(101),
                            (py + seconds * vy).rem_euclid(103),
                        )
                    })
                    .collect_vec(),
            )
        })
        .map(|(seconds, robots)| {
            (
                seconds,
                robots
                    .iter()
                    .counts_by(|r| r.0)
                    .into_values()
                    .max()
                    .unwrap(),
                robots
                    .iter()
                    .counts_by(|r| r.1)
                    .into_values()
                    .max()
                    .unwrap(),
            )
        })
        .find(|(_, mx, my)| *mx > 31 && *my > 33)
        .unwrap()
        .0
}
