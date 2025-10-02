aoc::main!();

fn preprocessing(input: &str) -> &str {
    input
}

fn part_1(input: &str) -> usize {
    solver(input, 4)
}

fn part_2(input: &str) -> usize {
    solver(input, 14)
}

fn solver(input: &str, size: usize) -> usize {
    (0..input.len() - size)
        .find_or_last(|n| input.to_string()[*n..n + size].chars().all_unique())
        .unwrap()
        + size
}
