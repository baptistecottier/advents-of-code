aoc::main!();

fn preprocessing(input: &str) -> Vec<&str> {
    input
    .lines()
    .collect()
}

fn part_1(strings: Vec<&str>) -> usize {
    strings
    .iter()
    .fold(0, |acc, l| acc  + l.len())
    -
    strings
    .iter()
    .map(|l| l.replace("\\\\","a").replace("\\\"", "a"))
    .fold(0, |acc , l| acc + l.len() - 3 * l.matches("\\x").count() - 2)
}

fn part_2(strings: Vec<&str>) -> usize {
    strings
    .iter()
    .map(|l| l.replace("\\","aa").replace("\"","aa"))
    .fold(0, |acc , l| acc + l.len() + 2)
    -
    strings
    .iter()
    .fold(0, |acc, l| acc  + l.len())
}