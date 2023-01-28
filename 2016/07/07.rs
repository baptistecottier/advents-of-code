aoc2016::main!(); 


fn generator(input: &str) -> Vec<[String;2]> {
    input
        .lines()
        .map(|l| l.split(['[',']']).collect_vec())
        .map(|l| [(0..=l.len()/2).map(|i| l[2 * i]).collect_vec().join(" "), 
                    (0..l.len()/2).map(|i| l[2 * i + 1]).collect_vec().join(" ")])
        .collect_vec()
}

fn part_1(input: Vec<[String;2]>) -> usize {
    solver(input, 4)
        .iter()
        .filter(|x| ! x[0].is_empty() && x[1].is_empty())
        .count() 
}

fn part_2(input: Vec<[String;2]>) -> usize {
    solver(input, 3)
        .iter()
        .filter(|x| iproduct!(x[0].chunks(3), x[1].chunks(3)).any(|(ca,cb)| ca[0] == cb[1] && ca[1] == cb[0]))
        .count()
}

fn solver(input: Vec<[String;2]>, size: usize) -> Vec<Vec<Vec<u8>>> {
    input
    .iter()
    .map(|ip| ip
        .iter()
        .map(|values| values
            .as_bytes()
            .windows(size)
            .filter(|w| w[0] == w[size - 1] && w[1] == w[size - 2] && w[0] != w[1])
            .map(|s| s.to_vec())
            .flatten()
            .collect())
        .collect_vec())
    .collect_vec()
}