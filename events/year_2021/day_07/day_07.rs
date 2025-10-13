aoc::main!();

fn preprocessing(input: &str) -> Vec<usize> {
    input
        .split(',')
        .map(|n| n.parse().unwrap())
        .sorted()
        .collect()
}

fn part_1(crabs: Vec<usize>) -> usize {
    crabs
        .iter()
        .map(|crab| crabs[crabs.len() / 2].abs_diff(*crab))
        .sum()
}

fn part_2(crabs: Vec<usize>) -> usize {
    crabs
        .iter()
        .map(|crab| mean(crabs.clone()).abs_diff(*crab))
        .map(|dist| dist * (dist + 1) / 2)
        .sum()
}

fn mean(numbers: Vec<usize>) -> usize {
    numbers.iter().sum::<usize>() / numbers.len()
}
