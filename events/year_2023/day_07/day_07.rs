aoc::main!();

fn preprocessing(input: &str) -> Vec<(String, usize)> {
    input
        .lines()
        .map(|hand| hand.split_once(' ').unwrap())
        .map(|(cards, bet)| (cards.to_string(), bet.parse().unwrap()))
        .collect()
}

fn part_1(bets: Vec<(String, usize)>) -> usize {
    winnings(bets, '∅')
}

fn part_2(bets: Vec<(String, usize)>) -> usize {
    winnings(bets, 'J')
}

fn winnings(bets: Vec<(String, usize)>, joker: char) -> usize {
    bets.iter()
        .map(|(cards, bet)| {
            (
                cards.chars().filter(|c| *c == joker).count(),
                cards
                    .chars()
                    .filter(|c| *c != joker)
                    .counts()
                    .into_values()
                    .sorted()
                    .rev()
                    .collect_vec(),
                cards
                    .chars()
                    .map(|c| {
                        format!("{} {}", joker, "23456789TJQKA".replace(joker, ""))
                            .chars()
                            .position(|cc| cc == c)
                            .unwrap()
                    })
                    .collect_vec(),
                bet,
            )
        })
        .map(|(jokers, hand_strength, cards_strength, bet)| {
            (
                5.min(jokers + hand_strength.iter().nth(0).unwrap_or(&0)),
                hand_strength.into_iter().skip(1).collect_vec(),
                cards_strength,
                bet,
            )
        })
        .sorted()
        .enumerate()
        .map(|(n, (_, _, _, b))| (n + 1) * b)
        .sum()
}
