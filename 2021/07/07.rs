aoc::main!();

fn preprocessing(input: &str) -> Vec<usize> {
    input
    .split(',')
    .map(|n| n.parse().unwrap())
    .collect()
}

fn part_1(crabs: Vec<usize>) -> usize {
    crabs
    .iter()
    .map(|crab| med(crabs.clone()).abs_diff(*crab))
    .sum()
}

fn part_2(crabs: Vec<usize>) -> usize {
    crabs
    .iter()
    .map(|crab| mean(crabs.clone()).abs_diff(*crab))
    .map(|dist| dist * (dist + 1) / 2)
    .sum()
}


fn med(numbers: Vec<usize>) -> usize {
    *numbers
    .iter()
    .sorted()
    .nth(numbers.len() / 2)
    .unwrap()
}

fn mean(numbers: Vec<usize>) -> usize {
    numbers
    .iter()
    .sum::<usize>()
    /
    numbers.len()
}
