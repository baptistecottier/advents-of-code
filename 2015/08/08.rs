aoc2015::main!();

fn generator(input : &str) -> Vec<&str> {
    input
        .lines()
        .collect()
}

fn part_1(input : Vec<&str>) -> usize {
    input
        .iter()
        .fold(0, |acc, l| acc  + l.len())
    -
    input
        .iter()
        .map(|l| l.replace("\\\\","a").replace("\\\"", "a"))
        .fold(0, |acc , l| acc +
            l.len()
            - 3*l.matches("\\x").count()
            - 2
                                                )
}

fn part_2(input : Vec<&str>) -> usize {
    input
        .iter()
        .map(|l| l.replace("\\","aa").replace("\"","aa"))
        .fold(0, |acc , l| acc +
                                                        l.len()
                                                        + 2
                                                    )
    -
    input
        .iter()
        .fold(0, |acc, l| acc  + l.len())
}