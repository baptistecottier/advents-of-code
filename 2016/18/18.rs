aoc::main!(); 

fn preprocessing(input: &str) -> Vec<bool> {
    input
    .chars()
    .map(|c| c == '^')
    .collect_vec()
}

fn part_1(tiles: Vec<bool>) -> usize {
    solver(tiles, 40)
}

fn part_2(tiles: Vec<bool>) -> usize {
    solver(tiles, 400000)
}

fn solver(tiles: Vec<bool>, rows: usize) -> usize {
    (0..rows - 1)
    .scan(tiles.to_vec(), |acc, _| {
        *acc = 
            [[false].to_vec(), acc.to_vec(), [false].to_vec()]
            .concat()
            .windows(3)
            .map(|w| w[0] ^ w[2])
            .collect_vec();
        Some(acc.clone())})
    .map(|s| s.iter().filter(|&&b| !b).count())
    .sum::<usize>()
    + tiles.iter().filter(|&b| !b).count()
}