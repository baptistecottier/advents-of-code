aoc::main!();

fn preprocessing(input: &str) -> Vec<Vec<u64>> {
    input
    .lines()
    .map(|row| row.chars().map(|c| if c == '#' {1} else {0}).collect_vec())
    .collect_vec()
}


fn part_1(trees: Vec<Vec<u64>>) -> u64 {
    traverse(trees, (3, 1))
}


fn part_2(trees: Vec<Vec<u64>>) -> u64 {
    [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    .iter()
    .map(|&slope| traverse(trees.clone(), slope))
    .product()
}


fn traverse(trees: Vec<Vec<u64>>, slope: (usize, usize)) -> u64 {
    trees
    .clone()
    .iter()
    .step_by(slope.1)
    .enumerate()
    .map(|(col, row)| row[(slope.0 * col) % (row.len())])
    .sum::<u64>()
}