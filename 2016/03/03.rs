aoc::main!();

fn preprocessing(input: &str) -> Vec<u16> {
    input
    .split([' ', '\n'])
    .filter_map(|n| n.parse::<u16>().ok())
    .collect_vec()
}

fn part_1(lengths : Vec<u16>) -> usize {
    solver(lengths, 1)
}

fn part_2(lengths : Vec<u16>) -> usize {
    solver(lengths, 3)
}


fn solver(lengths : Vec<u16>, shift: usize) -> usize {
    (0..lengths.len() / 3)
    .map(|t| ((t % shift) + (t / shift) * (3 * shift)))
    .map(|f| [lengths[f] , lengths[f + shift], lengths[f + 2 * shift]])
    .filter(|v| v.iter().sum::<u16>() > 2 * v.iter().max().unwrap())
    .count()
}