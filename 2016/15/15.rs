aoc2016::main!();

fn generator(input: &str) -> Vec<(i64, i64)> {
    input
    .lines()
    .map(|l| 
        l
        .split(&[' ', '.'])
        .into_iter()
        .filter_map(|n| n.parse().ok())
        .collect_tuple::<(i64, i64)>()
        .unwrap())
    .enumerate()
    .map(|(i, (n, a))| (n, - (i as i64 + a)))
    .collect_vec()
}

fn part_1(input: Vec<(i64, i64)>) -> i64 {
    chinese_remainder(input) - 1
}

fn part_2(input: Vec<(i64, i64)>) -> i64 {
    chinese_remainder([(input.iter().map(|l| l.0).product(), chinese_remainder(input) - 1),(11, -7)].to_vec())
}


fn egcd(a: i64, b: i64) -> (i64, i64, i64) {
    if a == 0 {
        (b, 0, 1)
    } else {
        let (g, x, y) = egcd(b % a, a);
        (g, y - (b / a) * x, x)
    }
}

fn mod_inv(x: i64, n: i64) -> i64 {
    egcd(x, n).1 % n
}

fn chinese_remainder(input: Vec<(i64, i64)>) -> i64 {
    let prod = input.iter().map(|v| v.0).product::<i64>();
    input
    .iter()
    .map(|(modulus, residue)| (modulus, residue, prod / modulus))
    .map(|(modulus, residue, p)| residue * mod_inv(p, *modulus) * p)
    .sum::<i64>()
    .rem_euclid(prod)
}