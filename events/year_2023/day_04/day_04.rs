aoc::main!();

fn preprocessing(input: &str) -> Vec<usize> {
    input
        .lines()
        .map(|game| {
            game.split(&[':', '|'])
                .skip(1)
                .map(|numbers| {
                    numbers
                        .split_whitespace()
                        .map(|number| number.parse::<u8>().unwrap())
                        .collect::<HashSet<u8>>()
                })
                .collect_tuple()
                .unwrap()
        })
        .map(|(draw, card)| draw.intersection(&card).count())
        .collect_vec()
}

fn part_1(input: Vec<usize>) -> usize {
    input.into_iter().map(|n| (1 << n) >> 1).sum()
}

fn part_2(input: Vec<usize>) -> usize {
    input
        .iter()
        .enumerate()
        .fold(vec![1; input.len()], |mut scratch, (game, score)| {
            (game..game + score).for_each(|gg| scratch[gg + 1] += scratch[game]);
            scratch
        })
        .iter()
        .sum()
}
