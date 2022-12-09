aoc2022::main!();

fn generator(input : &str) -> Vec<(i16, i16, i16, i16)> {
    input
        .lines()
        .map(|line| line.split(['-', ','])
            .map(|n| n.parse::<i16>().unwrap())
            .collect_tuple()
            .unwrap())
        .collect_vec()
}

fn part_1(assignements : Vec<(i16, i16, i16, i16)>) -> usize {
    solver(assignements)
}

fn part_2(assignements : Vec<(i16, i16, i16, i16)>) -> usize {
    solver(assignements.iter().map(|&(a,b,c,d)| (a,b,d,c)).collect_vec())
}

fn solver(input :  Vec<(i16, i16, i16, i16)>) -> usize{
    input
        .iter()
        .map(|(a, b, c, d)| ((a - c) * (b - d) <= 0) as usize)
        .sum()
}