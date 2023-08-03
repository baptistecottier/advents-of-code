aoc::main!();


fn parser(input: &str) -> Vec<(u32, u32, u32)> {
    input
    .lines()
    .map(|dimensions| 
        dimensions
        .split('x')
        .map(|n| n.parse().unwrap())
        .collect_tuple()
        .unwrap())
    .collect()
}

fn part_1(gifts : Vec<(u32, u32, u32)>) -> u32 {
    gifts
    .iter()
    .fold( 0, |acc , (l, w, h)| 
        acc 
        + 2 * (l * w + l * h + w * h) 
        + [l * w, l * h, w * h].iter().min().unwrap())
}

fn part_2(gifts : Vec<(u32, u32, u32)>)  -> u32{
    gifts
    .iter()
    .fold(0,  |acc, (l, w, h)| 
        acc 
        + l * w * h 
        + 2 * [l + w, l + h, h + w].iter().min().unwrap())
}
