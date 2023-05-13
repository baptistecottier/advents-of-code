aoc2016::main!(); 

fn generator(input: &str) -> Vec<bool> {
    input
    .chars()
    .map(|c| c == '^')
    .collect_vec()
}

fn part_1(input: Vec<bool>) -> usize {
    solver(input, 40)
}

fn part_2(input: Vec<bool>) -> usize {
    solver(input, 400000)
}

fn solver(input: Vec<bool>, rows: usize) -> usize {
    input.iter().filter(|&b| !b).count() +
    (0..rows - 1)
        .scan(input.to_vec(), |acc, _| {
            *acc = [[false].to_vec(), acc.to_vec(), [false].to_vec()]
            .concat()
            .windows(3)
            .map(|w| w[0] ^ w[2])
            .collect_vec();
            Some(acc.clone())})
        .map(|s| s.iter().filter(|&&b| !b).count())
        .sum::<usize>()
}