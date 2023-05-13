aoc2019::main!();

fn generator(input: &str) -> Vec<u32> {
    input
    .lines()
    .map(|n| n.parse().unwrap())
    .collect_vec()
}

fn part_1(input: Vec<u32>) -> u32 {
    compute_fuel(input)
    .iter()
    .sum()
}

fn part_2(input: Vec<u32>) -> u32 {
    (0..)
    .fold_while((compute_fuel(input), 0), |(fuel, total), _| {
        if fuel.len() == 0 {FoldWhile::Done((fuel, total))} 
        else { FoldWhile::Continue((compute_fuel(fuel.clone()), total + fuel.iter().sum::<u32>()))}})
    .into_inner()
    .1
}


fn compute_fuel(input: Vec<u32>) -> Vec<u32> {
    input
    .iter()
    .filter(|n| *n > &5)
    .map(|n| n / 3 - 2)
    .collect_vec()
}