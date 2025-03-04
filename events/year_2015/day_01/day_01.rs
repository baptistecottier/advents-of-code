aoc::main!();

fn preprocessing(input: &str) -> Vec<i32> {
    input
    .chars()
    .map(|direction| 
        match direction {
        '(' => 1,
        ')' => -1,
        _   => unreachable!()})
    .collect()
}

fn part_1(directions: Vec<i32>) -> i32 {
    directions
    .iter()
    .sum()
}

fn part_2(directions: Vec<i32>) -> usize {
    directions
    .iter()
    .scan(0, |floor, direction| {
        *floor += direction;
        Some(*floor)})
    .find_position(|n| *n < 0)
    .unwrap()
    .0
    + 1
}