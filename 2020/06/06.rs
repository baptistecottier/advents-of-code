aoc2020::main!();

fn generator(input: &str) -> Vec<Vec<&str>> {
    input
    .split("\n\n")
    .map(|group| group.split('\n').collect_vec())
    .collect_vec()
}

fn part_1(input: Vec<Vec<&str>>) -> usize {
    solver(input, 0)
}

fn part_2(input: Vec<Vec<&str>>) -> usize {
    solver(input, 1)
}

fn solver(groups: Vec<Vec<&str>>, all: usize) -> usize {
    groups
    .iter()
    .map(|group|
        group
        .iter()
        .join("")
        .chars()
        .counts()
        .iter()
        .filter(|(_,n)|
            **n >= all * group.len())
        .count())
    .sum()
}