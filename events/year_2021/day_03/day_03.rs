use num::pow;

aoc::main!();

fn preprocessing(input: &str) -> (usize, Vec<u16>) {
    (
        input.len() / (1 + input.chars().filter(|&c| c == '\n').count()),
        input
            .lines()
            .map(|l| u16::from_str_radix(l, 2).unwrap())
            .collect_vec(),
    )
}

fn part_1(input: (usize, Vec<u16>)) -> u16 {
    (0..input.0)
        .map(|n| pow(2, n))
        .map(|n| n * (input.1.iter().map(|v| v % n)));
    println!("{:?}", input.0);
    3
}

fn part_2(input: (usize, Vec<u16>)) -> u16 {
    3
}
