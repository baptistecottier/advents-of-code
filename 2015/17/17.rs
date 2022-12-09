aoc_2015::main!();

fn generator(input : &str) -> Vec<usize> {
    input
        .lines()
        .map(|n| n.parse::<usize>().unwrap())
        .collect_vec()
}

fn part_1(input : Vec<usize>) -> usize {
    solver(input)
        .iter()
        .sum()

}

fn part_2(input : Vec<usize>) -> usize {
    *solver(input)
        .iter()
        .find_or_first(|s| **s != 0)
        .unwrap()
}

fn solver(input : Vec<usize>) -> Vec<usize> {
    (3..=input.len())
    .map(|i|
        input
            .iter()
            .combinations(i)
            .filter(|c| c.iter().fold(0, |acc,b| acc + **b ) == 150)
            .count())
            .collect_vec()
}