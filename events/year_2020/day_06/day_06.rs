aoc::main!();

fn preprocessing(input: &str) -> Vec<(usize, HashMap<char, usize>)> {
    input
        .split("\n\n")
        .map(|group| {
            (
                group.lines().count(),
                group.replace("\n", "").chars().counts(),
            )
        })
        .collect_vec()
}

fn part_1(answers: Vec<(usize, HashMap<char, usize>)>) -> usize {
    answers.iter().map(|(_, cnts)| cnts.len()).sum()
}

fn part_2(answers: Vec<(usize, HashMap<char, usize>)>) -> usize {
    answers
        .iter()
        .map(|(grp_size, cnts)| cnts.values().filter(|&cnt| cnt == grp_size).count())
        .sum()
}
