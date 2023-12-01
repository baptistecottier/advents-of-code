use itertools::MinMaxResult;

aoc::main!();

fn preprocessing(input: &str) -> Vec<Vec<u16>> {
    input
    .lines()
    .map(|row| 
        row
        .split_whitespace()
        .map(|n| n.parse().unwrap())
        .collect_vec())
    .collect()
}

fn part_1(spreadsheet: Vec<Vec<u16>> ) -> u16 {
    spreadsheet
    .iter()
    .map(|row| row.iter().minmax())
    .map(|result| 
        match result {
            MinMaxResult::MinMax(a, b) => b - a ,
            _ => unreachable!()})
    .sum()
}

fn part_2(spreadsheet: Vec<Vec<u16>>) -> u16 {
    spreadsheet
    .iter()
    .map(|row| 
        row
        .iter()
        .permutations(2)
        .find(|pair| pair[0] % pair[1] == 0)
        .unwrap())
    .map(|pair,| pair[0] / pair[1])
    .sum()
}