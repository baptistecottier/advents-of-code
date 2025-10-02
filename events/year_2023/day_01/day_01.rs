aoc::main!();

fn preprocessing(input: &str) -> Vec<Vec<usize>> {
    input
        .lines()
        .map(|line| {
            AhoCorasick::new(&[
                "_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", "one", "two", "three",
                "four", "five", "six", "seven", "eight", "nine",
            ])
            .unwrap()
            .find_overlapping_iter(line)
            .map(|mat| mat.pattern().as_usize())
            .collect()
        })
        .collect()
}

fn part_1(document: Vec<Vec<usize>>) -> usize {
    document
        .iter()
        .map(|digits| digits.iter().filter(|&d| *d < 10))
        .map(|mut digits| digits.clone().nth(0).unwrap() * 10 + digits.nth_back(0).unwrap())
        .sum()
}

fn part_2(document: Vec<Vec<usize>>) -> usize {
    document
        .iter()
        .map(|digits| digits.iter().map(|d| d % 10))
        .map(|mut digits| digits.clone().nth(0).unwrap() * 10 + digits.nth_back(0).unwrap())
        .sum()
}
