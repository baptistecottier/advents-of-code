aoc2022::main!();

fn generator(input : &str) -> Vec<(u32, u32)> {
    input  
        .lines()
        .map(|l| (l.chars().nth(0).unwrap(),l.chars().nth(2).unwrap()))
        .map(|l| (l.0 as u32 - 63 , l.1 as u32 - 88))
        .collect_vec()
}

fn part_1(input : Vec<(u32, u32)>) -> u32 {
    solver(input, false)
}

fn part_2(input :Vec<(u32, u32)>) -> u32 {
    solver(input, true)
}

fn solver(input : Vec<(u32, u32)>, real_rules : bool) -> u32 {
    input
    .iter()
    .map(|l| [(l.1 + (1 + real_rules as u32) * 2 * l.0) % 3 , l.1])
    .map(|l| 3 * l[real_rules as usize] + l[!real_rules as usize] + 1)
    .sum()
}
