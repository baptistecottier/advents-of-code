aoc::main!();

fn preprocessing(input: &str) -> Vec<i32> {
    input
    .lines()
    .map(|change| change.parse().unwrap())
    .collect_vec()
}

fn part_1(changes: Vec<i32>) -> i32 {
    changes
    .iter()
    .sum()
}

fn part_2(changes: Vec<i32>) -> i32 {
    changes
    .iter()
    .cycle()
    .scan(0, |frequency, &change| {
        *frequency += change;
        Some(*frequency)})
    .duplicates()
    .nth(0)
    .unwrap()
}