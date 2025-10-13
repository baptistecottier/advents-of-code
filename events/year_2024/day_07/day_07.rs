aoc::main! {}

fn preprocessing(puzzle_input: &str) -> Vec<(u64, Vec<u64>)> {
    puzzle_input
        .lines()
        .map(|line| {
            line.split([' '])
                .map(|n| n.trim_end_matches(':').parse::<u64>().unwrap())
                .collect_vec()
        })
        .map(|v| match v.split_first() {
            Some((res, num)) => (*res, num.to_vec()),
            None => panic!("Expected at least one element in the vector"),
        })
        .collect()
}

fn part_1(equations: Vec<(u64, Vec<u64>)>) -> u64 {
    solver(equations, [add, mul])
}

fn part_2(equations: Vec<(u64, Vec<u64>)>) -> u64 {
    solver(equations, [add, mul, my_concat])
}

fn solver<const N: usize>(equations: Vec<(u64, Vec<u64>)>, ops: [fn(u64, u64) -> u64; N]) -> u64 {
    equations
        .iter()
        .filter(|(res, nums)| {
            let cands = nums.iter().fold(Vec::from([0]), |candidates, n| {
                candidates
                    .iter()
                    .map(|cand| ops.map(|f| f(*cand, *n)))
                    .flatten()
                    .filter(|n| n <= res)
                    .collect()
            });
            cands.contains(res)
        })
        .map(|(res, _)| *res)
        .sum()
}

fn add(a: u64, b: u64) -> u64 {
    a + b
}

fn mul(a: u64, b: u64) -> u64 {
    a * b
}

fn my_concat(a: u64, b: u64) -> u64 {
    a * 10u64.pow(b.ilog10() + 1) + b
}
