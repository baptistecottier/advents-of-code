aoc_2015::main!();


fn generator(input: &str) -> Vec<(u32, u32, u32)> {
    input
        .lines()
        .map(|l| {
            l.split('x')
                .map(|n| n.parse::<u32>().unwrap())
                .collect_tuple::<(_, _, _)>()
                .unwrap()
        })
        .collect()
}

fn part_1(gifts : Vec<(u32, u32, u32)>) -> u32 {
    gifts
        .iter()
        .fold( 0, |acc , g| 
            acc + 2 * (g.0 * g.1 + g.0 * g.2 + g.1 * g.2) + [g.0*g.1, g.0*g.2, g.1*g.2].iter().min().unwrap())
}

fn part_2(gifts : Vec<(u32, u32, u32)>)  -> u32{
    gifts
    .iter()
    .fold(0,  |acc, (l, w, h)| acc + l * w * h + 2 * [l+w,l+h,h+w].iter().min().unwrap())
}
