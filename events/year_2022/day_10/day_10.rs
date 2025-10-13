aoc::main!();

fn preprocessing(input: &str) -> Vec<i32> {
    input
        .lines()
        .map(|l| {
            if l == "noop" {
                (1, 0)
            } else {
                (2, l.split(' ').collect_vec()[1].parse().unwrap())
            }
        })
        .fold((Vec::new(), 1), |(c, v), (n, inc)| {
            ([c, repeat_n(v, n).collect_vec()].concat(), v + inc)
        })
        .0
}

fn part_1(ops: Vec<i32>) -> i32 {
    ops.iter()
        .enumerate()
        .filter(|(n, _)| ((*n as i32) - 19) % 40 == 0)
        .fold(0, |acc, (n, v)| acc + (1 + n as i32) * v)
}

fn part_2(ops: Vec<i32>) -> String {
    screen_reader(
        ops.iter()
            .enumerate()
            .map(|(n, &v)| {
                (
                    (n % 40, n / 40),
                    [v - 1, v, v + 1].contains(&((n as i32) % 40)),
                )
            })
            .filter(|(_, pred)| *pred)
            .map(|(coord, _)| coord)
            .collect(),
    )
}
