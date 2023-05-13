aoc2020::main!();

fn generator(input: &str) -> Vec<(usize, usize, char, &str)> {
    input
    .lines()
    .map(|l| l
        .split(['-',' ',':'])
        .collect_tuple()
        .unwrap())
    .map(|(a,b,c,_,d)| (a.parse().unwrap(), b.parse().unwrap(), c.chars().nth(0).unwrap(), d))
    .collect_vec()
}

fn part_1(input: Vec<(usize, usize, char, &str)>) -> usize {
    input
    .iter()
    .filter(|(a,b,c,d)| 
        (a..=b)
        .contains(&& d.chars().filter(|ch| ch == c)
        .count()))
    .count()
}

fn part_2(input: Vec<(usize, usize, char, &str)>) -> usize {
    input
    .iter()
    .filter(|&(a,b,c,d)| (d.chars().nth(a - 1).unwrap() == *c) ^ (d.chars().nth(b - 1).unwrap() == *c))
    .count()
}