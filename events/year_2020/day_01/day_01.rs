aoc::main!();

fn preprocessing(input: &str) -> Vec<u32> {
    input.lines().map(|l| l.parse().unwrap()).collect_vec()
}

fn part_1(expenses: Vec<u32>) -> u32 {
    iproduct!(expenses.clone(), expenses)
        .into_iter()
        .find(|(a, b)| a + b == 2020)
        .map(|(a, b)| a * b)
        .unwrap()
}

fn part_2(expenses: Vec<u32>) -> u32 {
    iproduct!(expenses.clone(), expenses.clone(), expenses)
        .into_iter()
        .find(|(a, b, c)| a + b + c == 2020)
        .map(|(a, b, c)| a * b * c)
        .unwrap()
}
