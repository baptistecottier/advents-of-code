aoc::main!();

fn preprocessing(input: &str) -> Vec<usize> {
    multizip(
        input
            .lines()
            .map(|line| line.split(':').nth(1).unwrap())
            .map(|line| {
                format!("{} {}", line.replace(' ', ""), line)
                    .split_whitespace()
                    .map(|n| n.parse().unwrap())
                    .collect_vec()
            })
            .collect_tuple::<(Vec<f64>, Vec<f64>)>()
            .unwrap(),
    )
    .map(|(time, distance)| {
        find_roots_quadratic(1.0, -1. * time, distance)
            .as_ref()
            .to_vec()
    })
    .map(|r| (r[1] as usize - r[0] as usize))
    .collect()
}

fn part_1(roots: Vec<usize>) -> usize {
    roots.iter().skip(1).product()
}

fn part_2(roots: Vec<usize>) -> usize {
    roots.into_iter().next().unwrap()
}
