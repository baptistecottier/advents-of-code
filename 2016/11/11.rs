aoc2016::main!();

fn generator(input: &str) -> Vec<usize> {
    input
        .lines()
        .map(|l| l
            .split(' ')
            .filter(|&w| ["microchip", "generator"].iter().any(|p| w.contains(p)))
            .count())
        .collect_vec()
}

fn part_1(input: Vec<usize>) -> usize {
    solver(input, 0)
}

fn part_2(input: Vec<usize>) -> usize {
    solver(input, 4)
}


fn solver(input: Vec<usize>, extra_parts: usize) -> usize {
    (1..4)
        .map(|n| 2 * (extra_parts + input.iter().take(n).sum::<usize>()) - 3)
        .sum()
}