aoc::main!();

fn preprocessing(input: &str) -> Vec<u64> {
    input.lines().map(|l| l.parse().unwrap()).collect_vec()
}

fn part_1(packages: Vec<u64>) -> u64 {
    solver(packages, 3)
}

fn part_2(packages: Vec<u64>) -> u64 {
    solver(packages, 4)
}

fn solver(packages: Vec<u64>, groups: u64) -> u64 {
    (0..(packages.len()) / (groups as usize))
        .map(|l| {
            packages
                .iter()
                .combinations(l)
                .filter(|c| {
                    c.iter().fold(0, |acc, &x| acc + *x)
                        == (packages.clone().iter().sum::<u64>() / groups)
                })
                .collect_vec()
        })
        .filter(|v| v.len() > 0)
        .next()
        .unwrap()
        .iter()
        .map(|c| c.iter().fold(1, |acc, &x| acc * *x))
        .min()
        .unwrap()
}
