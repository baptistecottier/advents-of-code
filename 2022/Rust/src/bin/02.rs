aoc2022::main!();

fn generator(input : &str) -> Vec<(u32, u32)> {
    input  
        .lines()
        .map(|l| (l.chars().nth(0).unwrap(),l.chars().nth(2).unwrap()))
        .map(|l| (l.0 as u32 - 63 , l.1 as u32 - 88))
        .collect_vec()
}

fn part_1(input : Vec<(u32, u32)>) -> u32 {
    solver(input, 1)
}

fn part_2(input :Vec<(u32, u32)>) -> u32 {
    solver(input, 2)
}

fn solver(input : Vec<(u32, u32)>, part : usize) -> u32 {
    input
    .iter()
    .map(|l| [(l.1 + (3 - part) as u32 * l.0) % 3 , l.1])
    .map(|l|  1 + 3 * l[(1 + part) % 2] + l[part % 2])
    .sum()
}
