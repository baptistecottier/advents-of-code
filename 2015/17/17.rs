aoc::main!();

fn parser(input: &str) -> Vec<usize> {
    input
    .lines()
    .map(|n| n.parse::<usize>().unwrap())
    .collect_vec()
}

fn part_1(containers : Vec<usize>) -> usize {
    solver(containers)
    .iter()
    .sum()

}

fn part_2(containers : Vec<usize>) -> usize {
    *solver(containers)
    .iter()
    .find_or_first(|s| **s != 0)
    .unwrap()
}

fn solver(containers : Vec<usize>) -> Vec<usize> {
    (3..=containers.len())
    .map(|i|
        containers
        .iter()
        .combinations(i)
        .filter(|c| c.iter().fold(0, |acc,b| acc + **b ) == 150)
        .count())
        .collect_vec()
}