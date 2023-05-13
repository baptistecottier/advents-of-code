aoc2021::main!(); 

fn generator(input: &str) -> Vec<u16> {
    input
    .lines()
    .map(|measurement| measurement.parse().unwrap())
    .collect_vec()
}

fn part_1(input: Vec<u16>) -> usize {
    solver(input, 1)
}

fn part_2(input: Vec<u16>) -> usize {
    solver(input, 3)
}

fn solver(measurements: Vec<u16>, delta: usize) -> usize {
    measurements
        .iter()
        .zip(measurements.iter().skip(delta))
        .filter(|(a, b)| a < b)
        .count()
}