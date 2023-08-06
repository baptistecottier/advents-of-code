aoc::main!();

fn preprocessing(input: &str) -> Vec<Vec<&str>> {
    input
    .lines()
    .map(|line| 
        line.split(' ').collect_vec())
    .collect_vec()
}

fn part_1(passphrases: Vec<Vec<&str>>) -> usize {
    passphrases
    .iter()
    .filter(|passphrase| 
        passphrase
        .iter()
        .all_unique())
    .count()
}

fn part_2(passphrases: Vec<Vec<&str>>) -> usize {
    passphrases
    .iter()
    .filter(|passphrase| 
        passphrase
        .iter()
        .map(|p| p.chars().sorted().collect_vec())
        .all_unique())
    .count()
}