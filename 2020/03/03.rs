aoc2020::main!();

fn generator(input: &str) -> Vec<Vec<u32>> {
    input
    .lines()
    .map(|row| row.chars().map(|c| if c == '#' {1} else {0}).collect_vec())
    .collect_vec()
}

fn part_1(input: Vec<Vec<u32>>) -> u32 {
    traverse(input, (3, 1))
}

fn part_2(input: Vec<Vec<u32>>) -> u32 {
    (1..=9)
    .step_by(2)
    .map(|i| traverse(input.clone(), (i % 8, 1 + i / 8)))
    .product()
}

fn traverse(trees: Vec<Vec<u32>>, slope: (usize, usize)) -> u32 {
    trees
    .clone()
    .iter()
    .step_by(slope.1)
    .enumerate()
    .map(|(i,row)| row[(slope.0 * i) % (row.len())])
    .sum::<u32>()
}