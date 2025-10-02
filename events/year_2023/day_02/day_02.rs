aoc::main!();

fn preprocessing(input: &str) -> Vec<Vec<(usize, usize)>> {
    input
        .lines()
        .map(|line| {
            Regex::new(r"([0-9]+)\s+(b|g|r)")
                .unwrap()
                .captures_iter(line)
                .map(|draw| draw.extract())
                .map(|(_, [n, c])| match c {
                    "b" => (n.parse().unwrap(), 0),
                    "g" => (n.parse().unwrap(), 1),
                    "r" => (n.parse().unwrap(), 2),
                    _ => unreachable!(),
                })
                .collect_vec()
        })
        .collect()
}

fn part_1(game: Vec<Vec<(usize, usize)>>) -> usize {
    game.iter()
        .enumerate()
        .filter(|(_, draws)| draws.iter().all(|(n, c)| n + c < 15))
        .map(|(n, _)| n + 1)
        .sum()
}

fn part_2(game: Vec<Vec<(usize, usize)>>) -> usize {
    game.iter()
        .map(|draws| {
            draws
                .iter()
                .fold((0, 0, 0), |(mb, mg, mr), (n, c)| match c {
                    0 => (mb.max(*n), mg, mr),
                    1 => (mb, mg.max(*n), mr),
                    2 => (mb, mg, mr.max(*n)),
                    _ => unreachable!(),
                })
        })
        .map(|(mb, mg, mr)| mb * mg * mr)
        .sum()
}
