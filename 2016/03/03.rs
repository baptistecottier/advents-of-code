aoc2016::main!();

fn generator(input: &str) -> Vec<u16> {
    input
        .split([' ', '\n'])
        .filter_map(|n| n.parse::<u16>().ok())
        .collect_vec()
}

fn part_1(input : Vec<u16>) -> usize {
    solver(input, 1)
}

fn part_2(input : Vec<u16>) -> usize {
    solver(input, 3)
}


fn solver(input : Vec<u16>, shift: usize) -> usize {
    (0..input.len() / 3)
        .map(|t| ((t % shift) + (t / shift) * (3 * shift)))
        .map(|f| [input[f] , input[f + shift], input[f + 2 * shift]])
        .filter(|v| v.iter().sum::<u16>() > 2 * v.iter().max().unwrap())
        .count()
}